# ================================================================================ #
#   Authors: Fabio Frazao and Oliver Kirsebom                                      #
#   Contact: fsfrazao@dal.ca, oliver.kirsebom@dal.ca                               #
#   Organization: MERIDIAN (https://meridian.cs.dal.ca/)                           #
#   Team: Data Analytics                                                           #
#   Project: ketos                                                                 #
#   Project goal: The ketos library provides functionalities for handling          #
#   and processing acoustic data and applying deep neural networks to sound        #
#   detection and classification tasks.                                            #
#                                                                                  #
#   License: GNU GPLv3                                                             #
#                                                                                  #
#       This program is free software: you can redistribute it and/or modify       #
#       it under the terms of the GNU General Public License as published by       #
#       the Free Software Foundation, either version 3 of the License, or          #
#       (at your option) any later version.                                        #
#                                                                                  #
#       This program is distributed in the hope that it will be useful,            #
#       but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#       GNU General Public License for more details.                               # 
#                                                                                  #
#       You should have received a copy of the GNU General Public License          #
#       along with this program.  If not, see <https://www.gnu.org/licenses/>.     #
# ================================================================================ #

""" Unit tests for the 'audio.audio_loader' module within the ketos library
"""
import pytest
import json
import os
import tarfile
import numpy as np
import pandas as pd
from pathlib import Path
from io import StringIO
from ketos.audio.waveform import Waveform, get_duration
from ketos.audio.spectrogram import MagSpectrogram
from ketos.audio.audio_loader import AudioLoader, AudioFrameLoader, AudioFrameEfficientLoader, SelectionTableIterator, ArchiveManager
from ketos.data_handling.selection_table import use_multi_indexing, standardize
from ketos.data_handling.data_handling import find_wave_files
from ketos.data_handling.parsing import parse_audio_representation
from ketos.audio.utils.misc import from_decibel

current_dir = os.path.dirname(os.path.realpath(__file__))
path_to_assets = os.path.join(os.path.dirname(current_dir),"assets")
path_to_tmp = os.path.join(path_to_assets,'tmp')


def test_init_audio_frame_loader_with_folder(five_time_stamped_wave_files):
    """ Test that we can initialize an instance of the AudioFrameLoader class from a folder"""
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.5)
    assert len(loader.selection_gen.files) == 5

def test_init_audio_frame_loader_with_wav_file(sine_wave_file):
    """ Test that we can initialize an instance of the AudioFrameLoader class 
        from a single wav file"""
    loader = AudioFrameLoader(filename=sine_wave_file, duration=0.5)
    assert len(loader.selection_gen.files) == 1
    assert loader.num() == 6

def test_init_audio_frame_loader_with_batches(sine_wave_file):
    """ Test that we can initialize an instance of the AudioFrameLoader class 
        from a single wav file with a batch size greater than 1"""
    loader = AudioFrameLoader(filename=sine_wave_file, duration=0.5, batch_size=2)
    assert len(loader.selection_gen.files) == 1
    assert loader.num() == 6

def test_init_audio_frame_efficient_loader_with_one_file(sine_wave_file):
    """ Test that we can initialize an instance of the AudioFrameEfficientLoader class 
        from a single wav file with a batch size equal to 1 file"""
    loader = AudioFrameEfficientLoader(filename=sine_wave_file, duration=0.5, num_frames='FILE')
    assert len(loader.selection_gen.files) == 1
    assert loader.num() == 6

def test_audio_frame_loader_gives_same_output_with_batches(sine_wave_file):
    """ Test that segments returned by the AudioFrameEfficientLoader class are independent of batch size"""
    rep = {'window':0.1,'step':0.02,'freq_max':800}
    fname = os.path.join(path_to_assets, 'grunt1.wav')
    loader1 = AudioFrameLoader(filename=fname, duration=0.4, step=0.12, representation=MagSpectrogram, representation_params=rep)
    loader3 = AudioFrameEfficientLoader(filename=fname, duration=0.4, step=0.12, representation=MagSpectrogram, representation_params=rep, num_frames=3)
    loaderf = AudioFrameEfficientLoader(filename=fname, duration=0.4, step=0.12, representation=MagSpectrogram, representation_params=rep, num_frames='file')
    for i in range(loader1.num()):
        x1 = next(loader1)
        x3 = next(loader3)
        xf = next(loaderf)
        dx = x1.data - x3.data
        assert np.mean(np.abs(dx)) < 0.1
        dx = x1.data - xf.data
        assert np.mean(np.abs(dx)) < 0.1

def test_audio_frame_loader_mag(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameLoader class to compute MagSpectrograms""" 
    rep = {'window':0.1,'step':0.02,'decibel':False}
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.5, representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 5
    assert loader.num() == 5
    s = next(loader)
    assert s.duration() == 0.5
    s = next(loader)
    assert s.duration() == 0.5
    assert loader.selection_gen.file_id == 2
    loader.reset()
    assert loader.selection_gen.file_id == 0

def test_audio_frame_loader_multiple_representations(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameLoader class to load multiple audio representations""" 
    rep1 = None
    rep2 = {'window':0.1,'step':0.02}
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.5, representation=[Waveform, MagSpectrogram], representation_params=[rep1, rep2])
    assert len(loader.selection_gen.files) == 5
    assert loader.num() == 5
    s = next(loader)
    assert len(s) == 2
    assert type(s[0]) == Waveform
    assert type(s[1]) == MagSpectrogram
    assert s[0].duration() == 0.5
    s = next(loader)
    assert s[1].duration() == 0.5
    assert loader.selection_gen.file_id == 2
    loader.reset()
    assert loader.selection_gen.file_id == 0

def test_audio_frame_loader_mag_in_batches(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameLoader class to compute MagSpectrograms 
        in batches""" 
    rep = {'window':0.1,'step':0.02, 'transforms':[]}
    loader_single = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.26, representation=MagSpectrogram, representation_params=rep)
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.26, representation=MagSpectrogram, representation_params=rep, batch_size=3)
    assert len(loader.selection_gen.files) == 5
    assert loader.num() == 10
    s = next(loader) 
    assert len(s) == 3
    assert loader.selection_gen.file_id == 1
    assert s[0].duration() == 0.26
    assert s[0].offset == 0
    assert s[1].duration() == 0.26
    assert s[1].offset == 0.26
    assert s[2].duration() == 0.26
    assert s[2].offset == 0
    s0 = next(loader_single)
    s1 = next(loader_single)
    s2 = next(loader_single)
    assert np.all(s0.get_data() == s[0].get_data())
    assert np.all(s1.get_data() == s[1].get_data())
    assert np.all(s2.get_data() == s[2].get_data())
    s = next(loader) 
    assert len(s) == 3
    s = next(loader) 
    assert len(s) == 3
    s = next(loader) 
    assert len(s) == 1 #last batch only has 1 spectrogram

def test_audio_frame_loader_mag_in_batches_1_file(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameEfficientLoader class to compute MagSpectrograms 
        in batches of 1 file per batch""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameEfficientLoader(path=five_time_stamped_wave_files, duration=0.12, representation=MagSpectrogram, representation_params=rep, num_frames='file')
    assert len(loader.selection_gen.files) == 5
    assert loader.num() == 25
    assert loader.selection_gen.file_id == 0
    s = next(loader) 
    assert loader.selection_gen.file_id == 1
    assert s.duration() == 0.12
    assert s.offset == 0
    s = next(loader)
    assert loader.selection_gen.file_id == 1
    assert s.duration() == 0.12
    assert s.offset == 0.12
    s = next(loader)
    s = next(loader)
    s = next(loader)
    assert loader.selection_gen.file_id == 1
    s = next(loader)
    assert loader.selection_gen.file_id == 2

def test_audio_frame_loader_norm_mag(sine_wave_file):
    """ Test that we can initialize the AudioFrameLoader class to compute MagSpectrograms
        with the normalize_wav option set to True""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameLoader(filename=sine_wave_file, duration=0.5, representation=MagSpectrogram, representation_params=rep)
    spec1 = next(loader)
    spec1 = next(loader)
    rep = {'window':0.1,'step':0.02, 'normalize_wav': True}
    loader = AudioFrameLoader(filename=sine_wave_file, duration=0.5, representation=MagSpectrogram, representation_params=rep)
    spec2 = next(loader)
    spec2 = next(loader)
    d1 = from_decibel(spec1.get_data())
    d2 = from_decibel(spec2.get_data()) / np.sqrt(2)
    assert np.all(np.isclose(np.mean(d1), np.mean(d2), rtol=2e-2))

def test_audio_frame_loader_mag_transforms(sine_wave_file):
    """ Test that we can initialize the AudioFrameLoader class to compute MagSpectrograms
        with various transformations applied""" 
    range_trans = {'name':'adjust_range', 'range':(0,1)}
    enh_trans = {'name':'enhance_signal','enhancement':2.3}
    transforms = [range_trans, enh_trans]
    norm_trans = {'name':'normalize','mean':0.5,'std':2.0}
    noise_trans = {'name':'add_gaussian_noise', 'sigma':2.0}
    wf_transforms = [norm_trans, noise_trans]
    rep = {'window':0.1,'step':0.02, 'transforms':transforms, 'waveform_transforms':wf_transforms}
    loader = AudioFrameLoader(filename=sine_wave_file, duration=0.5, representation=MagSpectrogram, representation_params=rep)
    spec1 = next(loader)
    assert spec1.transform_log == transforms
    assert spec1.waveform_transform_log == wf_transforms

def test_audio_frame_loader_dur(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameLoader class to compute MagSpectrograms
        with durations shorter than file durations""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.2, representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 5
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    assert loader.selection_gen.file_id == 1

def test_audio_frame_loader_overlap(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameLoader class to compute overlapping 
        MagSpectrograms""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.2, step=0.06, representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 5
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    assert loader.selection_gen.time == pytest.approx(3*0.06, abs=1e-6)
    assert loader.selection_gen.file_id == 0

def test_audio_frame_efficient_loader_overlap(five_time_stamped_wave_files):
    """ Test that we can use the AudioFrameEfficientLoader class to compute overlapping 
        MagSpectrograms""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameEfficientLoader(path=five_time_stamped_wave_files, duration=0.2, step=0.06, representation=MagSpectrogram, representation_params=rep, num_frames=2)
    assert len(loader.selection_gen.files) == 5
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    s = next(loader)
    assert s.duration() == 0.2
    assert loader.selection_gen.time == pytest.approx(5*0.06, abs=1e-6)
    assert loader.selection_gen.file_id == 0

def test_audio_frame_loader_uniform_length(five_time_stamped_wave_files):
    """ Check that the AudioFrameLoader always returns segments of the same length""" 
    rep = {'window':0.1,'step':0.02}
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.2, representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 5
    for _ in range(10):
        s = next(loader)
        assert s.duration() == 0.2

def test_audio_frame_loader_number_of_segments(sine_wave_file):
    """ Check that the AudioFrameLoader computes expected number of segments""" 
    rep = {'window':0.1,'step':0.01,'rate':2341}
    dur = get_duration(sine_wave_file)[0]
    # duration is an integer number of lengths
    l = 0.2
    loader = AudioFrameLoader(filename=sine_wave_file, duration=l, representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 1
    N = int(dur / l)
    assert N == loader.selection_gen.num_segs[0]
    # duration is *not* an integer number of lengths
    l = 0.21
    loader = AudioFrameLoader(filename=sine_wave_file, duration=l, representation=MagSpectrogram, representation_params=rep)
    N = int(np.ceil(dur / l))
    assert N == loader.selection_gen.num_segs[0]
    # loop over all segments
    for _ in range(N):
        _ = next(loader)
    # non-zero overlap
    l = 0.21
    o = 0.8*l
    loader = AudioFrameLoader(filename=sine_wave_file, duration=l, step=l-o, representation=MagSpectrogram, representation_params=rep)
    step = l - o
    N = int(np.ceil((dur-l) / step) + 1)
    assert N == loader.selection_gen.num_segs[0]
    # loop over all segments
    for _ in range(N):
        _ = next(loader)

def test_audio_loader_mag(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms""" 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1]],'start':[0.10,0.12],'end':[0.46,0.42]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep)
    assert loader.num() == 2
    s = next(loader)
    assert s.duration() == pytest.approx(0.36, abs=1e-6)
    s = next(loader)
    assert s.duration() == pytest.approx(0.30, abs=1e-6)

def test_audio_loader_can_skip(five_time_stamped_wave_files):
    """ Test that the audio loader can skip segments""" 
    rep = {'rate':1000}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1]],'start':[0.10,0.12],'end':[0.46,0.42]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=Waveform, representation_params=rep)
    assert loader.num() == 2
    loader.skip()
    s = next(loader)
    assert s.duration() == pytest.approx(0.30, abs=1e-6)

def test_audio_loader_with_labels(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms with labels""" 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1]],'start':[0.10,0.12],'end':[0.46,0.42],'label':[3,5]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep)
    s = next(loader)
    assert s.duration() == pytest.approx(0.36, abs=1e-6)
    assert s.label == 3
    s = next(loader)
    assert s.duration() == pytest.approx(0.30, abs=1e-6)
    assert s.label == 5

def test_audio_loader_with_annots(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        while including annotation data""" 
    rep = {'window':0.1,'step':0.02}
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    # create a selection table
    sel = pd.DataFrame({'filename':[files[0],files[1]],'start':[0.10,0.12],'end':[0.46,0.42]})
    sel = use_multi_indexing(sel, 'sel_id')
    # create a annotation table
    ann = pd.DataFrame({'filename':[files[0],files[0],files[1]],'label':[3,5,4],'start':[0.05,0.06,0.20],'end':[0.30,0.16,0.60]})
    ann = standardize(ann, labels={3:1, 5:3, 4:2})
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), annotations=ann, representation=MagSpectrogram, representation_params=rep)
    s = next(loader)
    assert s.duration() == pytest.approx(0.36, abs=1e-6)
    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start   end  freq_min  freq_max
0      1    -0.05  0.20       NaN       NaN
1      3    -0.04  0.06       NaN       NaN'''
# 0      0    -0.05  0.20       NaN       NaN
# 1      2    -0.04  0.06       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)
    s = next(loader)
    assert s.duration() == pytest.approx(0.30, abs=1e-6)
    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start  end  freq_min  freq_max
0      2   0.08  0.48       NaN       NaN'''
# 0      1   0.08  0.48       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)

def test_audio_loader_with_annots_subdirs():
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        while including annotation data when audio files are loaded from subfolders""" 
    rep = {'window':0.1,'step':0.02}
    path = os.path.join(path_to_assets, 'wav_files')
    filename1 = os.path.join('subf', 'w3.wav')
    # create a selection table
    sel = pd.DataFrame({'filename':[filename1, "w1.wav"],'start':[0.10,0.12],'end':[0.46,0.42]})
    # Standardizing paths using os.path.normpath
    sel = use_multi_indexing(sel, 'sel_id')
    # create a annotation table
  
    ann = pd.DataFrame({'filename':[filename1,filename1,"w1.wav"],'label':[3,5,4],'start':[0.05,0.06,0.20],'end':[0.30,0.16,0.60]})
    ann = standardize(ann, labels={3:1, 5:3, 4:2})
    
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=path, selection_table=sel), annotations=ann, representation=MagSpectrogram, representation_params=rep)
    s = next(loader)
    assert s.duration() == pytest.approx(0.36, abs=1e-6)
    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start   end  freq_min  freq_max
0      1    -0.05  0.20       NaN       NaN
1      3    -0.04  0.06       NaN       NaN'''
# 0      0    -0.05  0.20       NaN       NaN
# 1      2    -0.04  0.06       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)
    s = next(loader)
    assert s.duration() == pytest.approx(0.30, abs=1e-6)
    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start  end  freq_min  freq_max
0      2   0.08  0.48       NaN       NaN'''
# 0      1   0.08  0.48       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)

def test_audio_frame_loader_mag_json(five_time_stamped_wave_files, spectr_settings):
    """ Test that we can use the AudioFrameLoader class to compute MagSpectrograms from json settings""" 
    data = json.loads(spectr_settings)
    rep = parse_audio_representation(data['spectrogram'])
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, duration=0.5, representation=rep["type"], representation_params=rep)
    assert len(loader.selection_gen.files) == 5
    s = next(loader)
    assert s.duration() == 0.5
    s = next(loader)
    assert s.duration() == 0.5
    assert loader.selection_gen.file_id == 2

def test_audio_frame_loader_accepts_filename_list(five_time_stamped_wave_files, spectr_settings):
    """ Test that we can use the AudioFrameLoader class to compute MagSpectrograms from json settings""" 
    data = json.loads(spectr_settings)
    rep = parse_audio_representation(data['spectrogram'])
    filename = ['empty_HMS_12_ 5_ 0__DMY_23_ 2_84.wav', 
                'empty_HMS_12_ 5_ 1__DMY_23_ 2_84.wav',
                'empty_HMS_12_ 5_ 2__DMY_23_ 2_84.wav']
    loader = AudioFrameLoader(path=five_time_stamped_wave_files, filename=filename, duration=0.5, representation=rep["type"], representation_params=rep)
    assert len(loader.selection_gen.files) == 3
    s = next(loader)
    assert s.duration() == 0.5
    s = next(loader)
    assert s.duration() == 0.5
    assert loader.selection_gen.file_id == 2

def test_audio_loader_stores_source_data(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        and that the spectrograms retain the correct source data (filename, offset) """ 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    filename = [files[0],files[1]]
    start = [0.10,0.12]
    end = [0.46,0.42]
    sel = pd.DataFrame({'filename':filename,'start':start,'end':end})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep, stop=False)
    assert loader.num() == 2
    for i in range(6): #loop over each item 3 times
        s = next(loader)
        assert s.offset == start[i%2]
        assert s.filename == filename[i%2]

def test_audio_frame_loader_on_2min_wav():
    rep = {'window':0.2, 'step':0.02, 'window_func':'hamming', 'freq_max':600.}
    path = os.path.join(path_to_assets, '2min.wav')
    loader = AudioFrameLoader(filename=path, duration=30., step=15., representation=MagSpectrogram, representation_params=rep)
    assert loader.num() == 8
    s = next(loader)
    assert s.freq_max() == pytest.approx(600, abs=s.freq_res())

def test_audio_frame_loader_subdirs():
    """Test that loader can load audio files from subdirectories"""
    rep = {'window':0.2, 'step':0.02, 'window_func':'hamming', 'freq_max':1000.}
    path = os.path.join(path_to_assets, 'wav_files')
    loader = AudioFrameLoader(path=path, duration=30., step=15., representation=MagSpectrogram, representation_params=rep)
    assert len(loader.selection_gen.files) == 3
    assert loader.num() == 3
    s1 = next(loader)
    assert s1.filename == "subf/w3.wav"
    s2 = next(loader)
    assert s2.filename == "w1.wav"
    s3 = next(loader)
    assert s3.filename == "w2.wav"

def test_audio_loader_entire_files(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        of entire wav files """ 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':files})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep)
    assert loader.num() == 5
    for i in range(5):
        s = next(loader)
        assert s.duration() == 0.5

def test_audio_loader_with_attrs(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms with 
        extra attributes from selection table""" 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1]],
                        'start':[0.10,0.12],
                        'end':[0.46,0.42],
                        'comment':['big','small'],
                        'conf':[0.31,0.99]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader all attrs
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel, include_attrs=True), representation=MagSpectrogram, representation_params=rep)
    s = next(loader)
    attrs = s.get_instance_attrs()
    assert attrs['comment'] == 'big'
    assert attrs['conf'] == 0.31
    s = next(loader)
    attrs = s.get_instance_attrs()
    assert attrs['comment'] == 'small'
    assert attrs['conf'] == 0.99
    # init loader, selected attrs
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel, attrs=['comment','dummy']), representation=MagSpectrogram, representation_params=rep)
    s = next(loader)
    attrs = s.get_instance_attrs()
    assert attrs['comment'] == 'big'
    assert 'conf' not in attrs.keys()
    assert 'dummy' not in attrs.keys()

def test_audio_loader_accepts_kwargs(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms with 
        a complex phase""" 
    rep = {'window':0.1,'step':0.02}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1]],
                        'start':[0.10,0.12],
                        'end':[0.46,0.42],
                        'comment':['big','small'],
                        'conf':[0.31,0.99]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader all attrs
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep, compute_phase=True)
    s = next(loader)
    assert np.ndim(s.data) == 3

def test_audio_loader_start_end_outside_file(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        for selections that extend beyond the limits of the wav file """ 
    rep = {'window':0.02,'step':0.01}
    # create a selection table
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    sel = pd.DataFrame({'filename':[files[0],files[1],files[3]],
                        'start':[-0.20,0.12,0.44],
                        'end':[0.11,0.43,0.75]})
    sel = use_multi_indexing(sel, 'sel_id')
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), representation=MagSpectrogram, representation_params=rep)
    assert loader.num() == 3
    for i in range(3):
        s = next(loader)
        assert s.duration() == 0.31

def test_audio_loader_with_new_selection_table_style(five_time_stamped_wave_files):
    """ Test that we can use the AudioLoader class to compute MagSpectrograms
        for selections in the new (ketos3) selection table format where a single selection 
        may span several files""" 
    rep = {'window':0.02,'step':0.01}
    # gather the audio files
    files = find_wave_files(path=five_time_stamped_wave_files, return_path=False, search_subdirs=True)
    # create a selection table with two selections, the first of which spans two audio files
    sel = pd.DataFrame({'sel_id':  [0, 0, 1],
                        'filename':[files[0], files[1], files[1]],
                        'start':   [0.0, 0.0, 0.1],
                        'end':     [0.5, 0.2, 0.8]})
    sel.set_index(['sel_id', 'filename'], inplace=True)
    # create a annotation table
    ann = pd.DataFrame({'filename':[files[0], files[1], files[1]],
                        'label':[3, 5, 4],
                        'start':[0.05, 0.06, 0.20],
                        'end':  [0.30, 0.26, 0.60]})
    ann = standardize(ann, labels={3:1, 5:3, 4:2})
    # init loader
    loader = AudioLoader(selection_gen=SelectionTableIterator(data_dir=five_time_stamped_wave_files, selection_table=sel), annotations=ann, representation=MagSpectrogram, representation_params=rep)
    assert loader.num() == 2

    s = next(loader)
    assert np.isclose(s.duration(), 0.7, atol=1e-12)
    assert np.isclose(s.offset, 0.0, atol=1e-12)
    assert s.filename == os.path.basename(files[0])

    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start   end  freq_min  freq_max
0      1   0.05  0.30       NaN       NaN
1      3   0.56  0.76       NaN       NaN'''
#0      0   0.05  0.30       NaN       NaN
#1      2   0.56  0.76       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)

    s = next(loader)
    assert np.isclose(s.duration(), 0.7, atol=1e-12)
    assert np.isclose(s.offset, 0.1, atol=1e-12)
    assert s.filename == os.path.basename(files[1])

    #TODO: When we deprecate signal_labels and backgrnd labels from standardize method, change following line to:
    d = '''label  start   end  freq_min  freq_max
0      3   -0.04  0.16       NaN       NaN
1      2    0.10  0.50       NaN       NaN'''
#0      2   -0.04  0.16       NaN       NaN
#1      1   0.10  0.50       NaN       NaN'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    res = s.get_annotations()[ans.columns.values]
    pd.testing.assert_frame_equal(ans, res)

def test_audio_frame_loader_get_files():
    """Test that the get_file_paths method of the AudioFrameLoader class works"""
    path = os.path.join(path_to_assets, 'wav_files')
    loader = AudioFrameLoader(path=path, duration=30., step=15.)
    file_paths = loader.get_file_paths()
    expected = [os.path.join(path, 'subf', 'w3.wav'), os.path.join(path, 'w1.wav'), os.path.join(path, 'w2.wav')]
    assert file_paths == expected

def test_audio_frame_efficient_loader_with_transforms(growing_sine_wave_file):
    """ Test that transform are applied correctly to audio loaded with efficient method""" 
    norm_trans = {'name':'normalize','mean':0.5,'std':1.2}
    rep = {'transforms':[norm_trans]}
    loader = AudioFrameEfficientLoader(filename=growing_sine_wave_file, duration=0.04, representation=Waveform, representation_params=rep, num_frames=2)
    wf1_b = next(loader)
    wf2_b = next(loader)
    loader = AudioFrameEfficientLoader(filename=growing_sine_wave_file, duration=0.04, representation=Waveform, representation_params=rep, num_frames=1)
    wf1 = next(loader)
    wf2 = next(loader)
    np.testing.assert_array_almost_equal(wf1_b.get_data(), wf1.get_data())
    np.testing.assert_array_almost_equal(wf2_b.get_data(), wf2.get_data())


def test_archive_manager(tar_archive_with_wav_files):
    """ Test that we can use the ArchiveManager to extract audio files from a tar file """
    tar_path = tar_archive_with_wav_files
    m = ArchiveManager(tar_path)

    m.extract("w1.wav")
    assert os.path.exists(m.extract_dir)
    assert os.path.exists(os.path.join(m.extract_dir, "w1.wav"))
    assert len(find_wave_files(m.extract_dir)) == 1

    m.extract(["w1.wav", os.path.join("a","w2.wav")])
    assert os.path.exists(os.path.join(m.extract_dir, "w1.wav"))
    assert os.path.exists(os.path.join(m.extract_dir, os.path.join("a","w2.wav")))
    assert len(find_wave_files(m.extract_dir, search_subdirs=True)) == 2

    m.extract([os.path.join("a","w3.wav")])
    assert os.path.exists(os.path.join(m.extract_dir, os.path.join("a","w3.wav")))
    assert len(find_wave_files(m.extract_dir, search_subdirs=True)) == 1

    with pytest.warns(UserWarning):    
        m.extract("w4.wav")

    m.close()
    assert not os.path.exists(m.extract_dir)

def test_audio_loader_with_tar_archive(tar_archive_with_wav_files):
    """ Test that we can use the audio loader to load segments of wav files stored 
        within a tar archive """
    tar_path = tar_archive_with_wav_files
    rep = {'window':0.02,'step':0.01}

    # selection table
    sel = pd.DataFrame({'sel_id':  [0, 0, 1],
                        'filename':["w1.wav", os.path.join("a","w2.wav"), os.path.join("a",os.path.join("b","w1.wav"))],
                        'start':   [0.0, 0.0, 0.1],
                        'end':     [0.5, 0.2, 0.8]})
    sel.set_index(['sel_id', 'filename'], inplace=True)

    # audio loader
    sti = SelectionTableIterator(data_dir=tar_path, selection_table=sel)
    loader = AudioLoader(selection_gen=sti, representation=MagSpectrogram, representation_params=rep)

    assert loader.num() == 2

    x = next(loader)
    assert np.abs(x.duration() - 0.7) < 1e-12

    x = next(loader)
    assert np.abs(x.duration() - 0.7) < 1e-12

    sti.reset() #ensures that the extraction directory gets removed