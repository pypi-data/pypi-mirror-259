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

""" Unit tests for the selection_table module within the ketos library
"""
import pytest
import os
import ketos.data_handling.selection_table as st
import pandas as pd
import numpy as np
from io import StringIO
import datetime as dt
import tempfile


current_dir = os.path.dirname(os.path.realpath(__file__))
path_to_assets = os.path.join(os.path.dirname(current_dir),"assets")
path_to_tmp = os.path.join(path_to_assets,'tmp')


def test_trim():
    standard = ['filename','label','start','end','freq_min','freq_max']
    extra = ['A','B','C']
    df = pd.DataFrame(columns=extra)
    df = st.trim(df)
    assert len(df.columns) == 0
    df = pd.DataFrame(columns=standard+extra)
    df = st.trim(df)
    assert sorted(df.columns.values) == sorted(standard)

def test_is_standardized():
    df = pd.DataFrame({'filename':'test.wav','label':[1],'start':[0],'end':[2],'freq_min':[None],'freq_max':[None]})
    df = st.standardize(df)
    assert st.is_standardized(df) == True
    df = pd.DataFrame({'filename':'test.wav','label':[1]})
    df = st.standardize(df)
    assert st.is_standardized(df) == True
    df = pd.DataFrame({'filename':'test.wav','label':[1]})
    assert st.is_standardized(df) == False


def test_empty_annotation_table():
    df = st.empty_annot_table()
    assert len(df) == 0
    assert np.all(df.columns == ['label', 'start', 'end'])
    assert df.index.names == ['filename', 'annot_id']


def test_empty_selection_table():
    df = st.empty_selection_table()
    assert len(df) == 0
    assert np.all(df.columns == ['label', 'start', 'end', 'annot_id'])
    assert df.index.names == ['filename', 'sel_id']


def test_create_label_dict():
    l1 = [0, 'gg', -17, 'whale']
    l2 = [999]
    d = st._create_label_dict(l1, l2)
    ans = {999: -1, 0: 0, 'gg':1, -17: 2, 'whale': 3}
    assert d == ans


def test_create_label_dict_can_handle_nested_list():
    l1 = [[-33, 1, 'boat']]
    l2 = [0, 'gg', [-17, 'whale']]   
    l3 = [999]
    d = st._create_label_dict(l1+l2, l3)
    ans = {-33: 0, 1:0, 'boat': 0, 999: -1, 0: 1, 'gg':2, -17: 3, 'whale': 3}
    assert d == ans


def test_unfold(annot_table_mult_labels):
    res = st.unfold(annot_table_mult_labels)
    ans = pd.DataFrame({'filename':['f0.wav','f0.wav','f1.wav'], 'label':['1','2','3'], 'start':[0,0,1], 'end':[1,1,2]})
    res = res.reset_index(drop=True)[ans.columns]
    pd.testing.assert_frame_equal(ans, res[ans.columns.values])

def test_standardize_with_dataframe_input(basic_dataframe):
    """
    Test standardization with a pandas DataFrame input. Verifies that the function returns
    a DataFrame, it's not empty, and the index includes 'filename' and 'annot_id'.
    """
    result = st.standardize(annotations=basic_dataframe)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'filename' in result.index.names
    assert 'annot_id' in result.index.names

def test_standardize_with_csv_input(temp_csv_file):
    """
    Test standardization with a CSV file input. Verifies that the function returns
    a DataFrame, it's not empty, and cleans up the temporary CSV file after testing.
    """
    result = st.standardize(annotations=temp_csv_file)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    os.remove(temp_csv_file)  # Cleanup

def test_standardize_automatic_label_mapping(basic_dataframe):
    """
    Test automatic label mapping during standardization. Verifies that labels are correctly
    mapped to integers, the data columns match expected values, and the 'label_dict' attribute
    contains the correct mappings for 'dolphin' and 'whale'.
    """
    result = st.standardize(annotations=basic_dataframe, labels='auto')
    # Expected data columns, ignoring the index for now
    expected_data = {
        'label': [1, 0],  # Assuming 'dolphin'->'0', 'whale'->'1' after auto mapping
        'start': [0., 5.],
        'end': [10., 15.],
    }
    expected_df = pd.DataFrame(expected_data, index=pd.MultiIndex.from_arrays([
        ['file1', 'file2'],  # filename
        [0, 0]  
    ], names=['filename', 'annot_id']))
  
    # Check data columns match
    pd.testing.assert_frame_equal(result[['label', 'start', 'end']], expected_df[['label', 'start', 'end']])

    # Check the first level of the index (filename) matches
    assert (result.index.get_level_values('filename') == expected_df.index.get_level_values('filename')).all()

    assert sorted(result.attrs['label_dict'].keys()) == ['dolphin', 'whale']

def test_standardize_dict_label_mapping(basic_dataframe):
    """
    Test custom dictionary label mapping during standardization. Verifies that labels are
    correctly mapped according to the provided dictionary.
    """
    custom_labels = {'whale': 1, 'dolphin': 2}
    result = st.standardize(annotations=basic_dataframe, labels=custom_labels)
    assert all(result['label'].map(int).isin([1, 2]))

def test_standardize_no_label_mapping(basic_dataframe):
    """
    Test standardization with no label mapping (labels=None). Verifies that labels
    remain unchanged in the result.
    """
    result = st.standardize(annotations=basic_dataframe, labels=None)
    # Verify labels remain unchanged
    assert sorted(result['label'].unique()) == ['dolphin', 'whale']

def test_standardize_list_of_labels(varied_labels_dataframe):
    """
    Test standardization with a list of labels for mapping. Verifies that labels not
    in the list are mapped to -1, and the 'label_dict' only includes specified labels.
    """
    # Specify only a subset of labels to map
    labels_list = ['whale', 'dolphin']
    result = st.standardize(annotations=varied_labels_dataframe, labels=labels_list)
    # Expect 'shark' to be mapped to -1
    mapped_labels = result['label'].map(int).unique()
    assert sorted(mapped_labels) == [-1, 0, 1]  # 'shark' becomes -1, 'whale' and 'dolphin' are 0 and 1
    # Verify that 'label_dict' only includes specified labels
    assert 'shark' not in result.attrs['label_dict']

def test_standardize_unfold_labels(multi_label_dataframe):
    """
    Test unfolding multiple labels per row during standardization. Verifies that
    rows with multiple labels are correctly unfolded into separate rows.
    """
    result = st.standardize(annotations=multi_label_dataframe, unfold_labels=True, labels=None, label_sep=',')
    assert len(result) == 2  # Two labels should result in two rows

def test_standardize_trim_table(basic_dataframe):
    """
    Test trimming of extra columns during standardization. Verifies that only
    columns relevant to the standardized format are retained in the result.
    """
    basic_dataframe['extra_column'] = 'extra'
    result = st.standardize(annotations=basic_dataframe, trim_table=True)
    assert 'extra_column' not in result.columns

def test_standardize_datetime_format(datetime_dataframe):
    """
    Test handling of datetime format during standardization. Verifies that datetime
    columns are correctly parsed according to the specified format.
    """
    result = st.standardize(annotations=datetime_dataframe, datetime_format='%d_%m_%Y')
    assert pd.to_datetime(result['datetime']).dt.year.eq(2020).all()

def test_standardize_invalid_input_type():
    """
    Test standardization with an invalid input type. Verifies that the function
    raises a ValueError when input is not a DataFrame or a file path.
    """
    with pytest.raises(ValueError):
        st.standardize(annotations=123)

def test_standardize_missing_required_columns():
    """
    Test standardization with missing required columns in the input DataFrame.
    Verifies that the function raises an AssertionError when required columns
    are missing.
    """
    df = pd.DataFrame({'wrong_column': [1, 2]})
    with pytest.raises(AssertionError):
        st.standardize(annotations=df, labels=None)

def test_standardize_datetime():
    """ Test that datetime information is parsed correctly
    """
    filenames = ["empty_HMS_12_ 5_28__DMY_23_ 2_1984.wav",
                 "empty_HMS_12_05_28__DMY_23_03_1924.wav",
                 "subfolder/empty_HMS_23_05_28__DMY_23_ 1_1924.wav"]
    labels = [0,1,2]
    fmt = '*HMS_%H_%M_%S__DMY_%d_%m_%Y*'
    # datetime field not specified (defaults to filename)
    tbl = pd.DataFrame({'filename':filenames,'label':labels})
    res = st.standardize(tbl, datetime_format=fmt)
    assert res['datetime'][0] == dt.datetime(1984, 2, 23, 12, 5, 28) 
    assert res['datetime'][1] == dt.datetime(1924, 3, 23, 12, 5, 28) 
    assert res['datetime'][2] == dt.datetime(1924, 1, 23, 23, 5, 28) 
    # datetime field specified
    t = [os.path.basename(f) for f in filenames]
    tbl = pd.DataFrame({'filename':filenames,'label':labels,'datetime':t})
    res = st.standardize(tbl, datetime_format=fmt)
    assert res['datetime'][0] == dt.datetime(1984, 2, 23, 12, 5, 28) 
    assert res['datetime'][1] == dt.datetime(1924, 3, 23, 12, 5, 28) 
    assert res['datetime'][2] == dt.datetime(1924, 1, 23, 23, 5, 28) 
    tbl = pd.DataFrame({'filename':filenames,'label':labels,'datetime':t})
    res = st.standardize(tbl, datetime_format=fmt)
    assert res['datetime'][0] == dt.datetime(1984, 2, 23, 12, 5, 28) 
    assert res['datetime'][1] == dt.datetime(1924, 3, 23, 12, 5, 28) 
    assert res['datetime'][2] == dt.datetime(1924, 1, 23, 23, 5, 28) 


def test_label_occurrence(annot_table_std):
    df = annot_table_std
    oc = st.label_occurrence(df)
    ans = {-1: 1, 0: 2, 1: 1, 2: 1, 3: 1}
    assert oc == ans


def test_select_center(annot_table_std):
    df = st.standardize(annot_table_std)
    print(df)
    # request length shorter than annotations
    res = st.select(df, length=1, center=True)
    d = '''filename sel_id label  start   end
f0.wav   0           2   1.15  2.15
f0.wav   1           1   4.15  5.15
f1.wav   0           3   2.15  3.15
f1.wav   1           1   5.15  6.15
f2.wav   0           4   3.15  4.15
f2.wav   1           0   6.15  7.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, res[ans.columns.values])
    # request length longer than annotations
    res = st.select(df, length=5, center=True)
    d = '''filename sel_id  label  start   end
f0.wav   0           2  -0.85  4.15
f0.wav   1           1   2.15  7.15
f1.wav   0           3   0.15  5.15
f1.wav   1           1   3.15  8.15
f2.wav   0           4   1.15  6.15
f2.wav   1           0   4.15  9.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, res[ans.columns.values])


def test_select_ignores_annotations_with_label_minus_1(annot_table_std):
    df = annot_table_std
    df = st.standardize(df)
    res = st.select(df, length=1, center=True)
    assert len(res[res.label==-1]) == 0


def test_select_only_uses_specified_labels(annot_table_std):
    df = st.standardize(annot_table_std)
    res = st.select(df, length=1, center=True, label=[0,2])
    assert np.all(np.isin(res.label.values, [0,2]))


def test_select_avoids_certain_labels(annot_table_std):
    df = st.standardize(annot_table_std)
    res = st.select(df, length=3.3, center=True, label=[1,3], avoid_label=[2])
    assert np.all(np.isin(res.label.values,[1,3]))
    assert len(res) == 2
    res.reset_index(inplace=True)
    res.iloc[0].to_dict() == {'filename': 'f1.wav', 'sel_id': 0, 'label': 3, 'start': 1.0, 'end': 4.3}
    res.iloc[1].to_dict() == {'filename': 'f1.wav', 'sel_id': 0, 'label': 1, 'start': 4.0, 'end': 7.3}
    res = st.select(df, length=3.3, center=True, label=[1,3,0], avoid_label="ALL")
    assert np.all(np.isin(res.label.values,[1,3,0]))
    assert len(res) == 2


def test_select_discards_selections_outside_file(annot_table_std):
    df = st.standardize(annot_table_std)
    files = pd.DataFrame({'filename':['f0.wav','f1.wav','f2.wav'], 'duration':[10,10,10]})
    res = st.select(df, length=7.0, center=True, discard_outside=True, files=files)
    assert len(res) == 3


def test_select_keeps_extra_attrs(annot_table_std):
    annot_table = annot_table_std.copy()
    annot_table['comment'] = ['good', 'tall', 'thin', 'bad', 'hopeless', 'green'] #add extra column
    df = annot_table
    df = st.standardize(df)
    res = st.select(df, length=1, center=True)
    assert 'comment' in res.columns.values


def test_select_enforces_overlap(annot_table_std):
    np.random.seed(3)
    df = annot_table_std
    df = st.standardize(df)
    # requested length: 5.0 sec
    # all annotations have duration: 3.3 sec  (3.3/5.0=0.66)
    length = 5.0
    overlap = 0.5
    df_new = st.select(df, length=length, min_overlap=overlap, keep_id=True)
    t1 = df_new.start.values
    t2 = df_new.end.values
    idx = zip(df_new.index.get_level_values(0), df_new.annot_id)
    df = df.loc[idx]
    t2_orig = df.end.values
    t1_orig = df.start.values
    assert np.all(t2 >= t1_orig + overlap * length)
    assert np.all(t1 <= t2_orig - overlap * length)


def test_select_step(annot_table_std):
    df = annot_table_std
    df = st.standardize(df)
    N = len(df[df['label']!=-1])
    K = len(df[df['label']==5])
    df_new = st.select(df, length=1, center=True, min_overlap=0, step=0.5, keep_id=True)
    M = len(df_new)
    assert M == (N - K) * (2 * int((3.3/2+0.5)/0.5) + 1) + K * (2 * int((3.3/2-0.5)/0.5) + 1)
    df_new = st.select(df, length=1, center=True, min_overlap=0.4, step=0.5)
    M = len(df_new)
    assert M == (N - K) * (2 * int((3.3/2+0.5-0.4)/0.5) + 1) + K * (2 * int((3.3/2-0.5)/0.5) + 1)

def test_select_warning_annotation_error(annot_table_std):
    """ Test that a warning is given when an annotation contains a start time greater than end time
    and that select ignores the annotation
    """
    np.random.seed(2)
    df = annot_table_std
    df["end"][1] = 0.23
    df = st.standardize(df)

    with pytest.warns(UserWarning):
        res = st.select(annotations=df, length=1.0, center=False)

    d ='''filename sel_id label start end                            
f0.wav   0           2  1.002788  2.002788
f0.wav   1           1  3.059630  4.059630
f1.wav   1           1  5.264224  6.264224
f2.wav   0           4  3.001242  4.001242
f2.wav   1           0  5.966846  6.966846'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, res[ans.columns.values])


def test_time_shift():
    row = pd.Series({'label':3.00,'start':0.00,'end':3.30,'annot_id':0.00,'length':3.30,'start_new':-0.35})
    res = st.time_shift(annot=row, time_ref=row['start_new'], length=4.0, min_overlap=0.8, step=0.5)
    d = '''label  start  end  annot_id  length  start_new
0    3.0    0.0  3.3       0.0     3.3      -1.35
1    3.0    0.0  3.3       0.0     3.3      -0.85
2    3.0    0.0  3.3       0.0     3.3      -0.35
3    3.0    0.0  3.3       0.0     3.3       0.15
4    3.0    0.0  3.3       0.0     3.3       0.65'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0])
    pd.testing.assert_frame_equal(ans, res[ans.columns.values])

def test_time_shift_negative_length_raises_exception():
    """ Test that the assertion error for a length smaller than 0 is thrown
    """
    annot = {'filename':'file1.wav', 'label':1, 'start':12.0, 'end':14.0}

    with pytest.raises(AssertionError):
        st.time_shift(annot, time_ref=13.0, length=-1.0, step=0.2, min_overlap=0.5)

def test_time_shift_positive_length_doesnt_raises_exception():
    """ Test that the assertion error is not thrown for good values
    """
    annot = {'filename':'file1.wav', 'label':1, 'start':12.0, 'end':14.0}

    try:
        st.time_shift(annot, time_ref=13.0, length=1.0, step=0.2, min_overlap=0.5)
    except AssertionError as exc:
        assert False, f"'time_shift' raised an exception {exc}"

def test_select_with_varying_overlap(annot_table_std):
    """ Test that the number of selections increases as the 
        minimum required overlap is reduced"""
    df = st.standardize(annot_table_std)
    # request length shorter than annotations
    num_sel = []
    for min_overlap in np.linspace(1.0, 0.0, 11):
        res = st.select(df, length=1.0, step=0.5, center=True, min_overlap=min_overlap)
        num_sel.append(len(res))
    
    assert np.all(np.diff(num_sel) >= 0)
    # request length longer than annotations
    num_sel = []
    for min_overlap in np.linspace(1.0, 0.0, 11):
        res = st.select(df, length=4.0, step=0.5, center=True, min_overlap=min_overlap)
        num_sel.append(len(res))

    assert np.all(np.diff(num_sel) >= 0)


def test_create_rndm_selections_with_label(file_duration_table):
    np.random.seed(1)
    dur = file_duration_table 
    num = 5
    df_bgr = st.create_rndm_selections(files=dur, length=2.0, num=num, label=6)
    assert len(df_bgr) == num
    # assert selections have uniform length
    assert np.all(np.isclose(df_bgr.end.values - df_bgr.start.values, 2.0, atol=1e-9))
    # assert all selection have label = 6
    assert np.all(df_bgr.label.values == 6)




def test_create_rndm_selections_with_empty_annot(file_duration_table):
    """ Test if can generate a random selection with an empty annotation table"""
    np.random.seed(1)
    dur = file_duration_table 
    num = 5
    df = st.empty_annot_table()
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=num)
    assert len(df_bgr) == num
    # assert selections have uniform length
    assert np.all(np.isclose(df_bgr.end.values - df_bgr.start.values, 2.0, atol=1e-9))
    # assert all selection have label = 0
    assert np.all(df_bgr.label.values == 0)


def test_create_rndm_selections_with_empty_file_duration_table():
    """ Test if can generate a random selection with an empty annotation table"""
    np.random.seed(1)
    num = 5
    df = st.empty_annot_table()
    dur = pd.DataFrame(columns=['filename','duration'])
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=num)
    assert len(df_bgr) == 0


def test_create_rndm_selections_with_annot(annot_table_std, file_duration_table):
    """ Test if can generate a random selection while avoiding annotated regions of the recording"""
    np.random.seed(1)
    df = st.standardize(annot_table_std)
    dur = file_duration_table 
    num = 5
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, label=10, length=2.0, num=num)
    assert len(df_bgr) == num
    # assert selections have uniform length
    assert np.all(np.abs(df_bgr.end.values - df_bgr.start.values - 2.0) < 1e-9)
    # assert all selection have label = 10
    assert np.all(df_bgr.label.values == 10)
    # assert selections do not overlap with any annotations
    for bgr_idx, bgr_sel in df_bgr.iterrows():
        start_bgr = bgr_sel.start
        end_bgr = bgr_sel.end
        fname = bgr_idx[0]
        q = st.query(df, start=start_bgr, end=end_bgr, filename=fname)
        assert len(q) == 0


def test_create_rndm_keeps_misc_cols(annot_table_std, file_duration_table):
    """ Check that the random selection creation method keeps 
        any miscellaneous columns"""
    np.random.seed(1)
    df = st.standardize(annot_table_std)
    dur = file_duration_table 
    dur['extra'] = 'testing'
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=5)
    assert np.all(df_bgr['extra'].values == 'testing')
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=5, trim_table=True)
    assert 'extra' not in df_bgr.columns.values.tolist()


def test_create_rndm_files_missing_duration(annot_table_std, file_duration_table):
    """ Check that the random selection creation method works even when 
        some of the files are missing from the file duration list"""
    np.random.seed(1)
    df = st.standardize(annot_table_std)
    dur = file_duration_table.drop(0) 
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=11)


def test_create_rndm_nonzero_offset(annot_table_std, file_duration_table):
    """ Check that the random selection creation method works when file duration 
        table includes offsets"""
    np.random.seed(1)
    df = st.standardize(annot_table_std)
    file_duration_table['offset'] = [1, 2, 3, 4, 5, 6]
    df_bgr = st.create_rndm_selections(annotations=df, files=file_duration_table, length=2.0, num=11)


def test_create_rndm_selections_no_overlap(annot_table_std, file_duration_table):
    """ Check that random selections have no overlap"""
    np.random.seed(1)
    df = st.standardize(annot_table_std)
    dur = file_duration_table 
    num = 30
    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=num)
    num_overlap = 0
    for idx,row in df_bgr.iterrows():
        q = st.query(df_bgr, filename=idx[0], start=row['start'], end=row['end'])
        num_overlap += len(q) - 1
    
    assert num_overlap > 0

    df_bgr = st.create_rndm_selections(annotations=df, files=dur, length=2.0, num=num, no_overlap=True)
    num_overlap = 0
    for idx,row in df_bgr.iterrows():
        q = st.query(df_bgr, filename=idx[0], start=row['start'], end=row['end'])
        num_overlap += len(q) - 1
    
    assert num_overlap == 0


def test_select_by_segmenting(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table
    sel = st.select_by_segmenting(f, length=5.1, annotations=a, step=4.0, discard_empty=True, pad=True)
    # check selection table
    d = '''filename sel_id start  end
f0.wav   0         0.0  5.1
f0.wav   1         4.0  9.1
f1.wav   0         0.0  5.1
f1.wav   1         4.0  9.1
f2.wav   0         0.0  5.1
f2.wav   1         4.0  9.1
f2.wav   2         8.0 13.1'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, sel[0][ans.columns.values])
    # check annotation table
    d = '''filename sel_id annot_id label  start  end
f0.wav   0      0             2         0.0        3.3
f0.wav   0      1             1         3.0        6.3
f0.wav   1      1             1        -1.0        2.3
f1.wav   0      0             3         1.0        4.3
f1.wav   0      1             1         4.0        7.3
f1.wav   1      0             3        -3.0        0.3
f1.wav   1      1             1         0.0        3.3
f2.wav   0      0             4         2.0        5.3
f2.wav   0      1             0         5.0        8.3
f2.wav   1      0             4        -2.0        1.3
f2.wav   1      1             0         1.0        4.3
f2.wav   2      1             0        -3.0        0.3'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1,2])
    pd.testing.assert_frame_equal(ans, sel[1][ans.columns.values])


def test_select_by_segmenting_keep_only_empty(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table
    sel = st.select_by_segmenting(f, length=16.0, annotations=a, step=4.0, keep_only_empty=True, pad=False)
    # check selection table
    d = '''filename sel_id start  end
f0.wav   2         8.0  24.0
f0.wav   3        12.0  28.0
f1.wav   2         8.0  24.0
f1.wav   3        12.0  28.0
f2.wav   3        12.0  28.0
f2.wav   4        16.0  32.0
f3.wav   0         0.0  16.0
f3.wav   1         4.0  20.0
f3.wav   2         8.0  24.0
f3.wav   3        12.0  28.0
f3.wav   4        16.0  32.0
f4.wav   0         0.0  16.0
f4.wav   1         4.0  20.0
f4.wav   2         8.0  24.0
f4.wav   3        12.0  28.0
f4.wav   4        16.0  32.0
f5.wav   0         0.0  16.0
f5.wav   1         4.0  20.0
f5.wav   2         8.0  24.0
f5.wav   3        12.0  28.0
f5.wav   4        16.0  32.0'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, sel[ans.columns.values])


def test_select_by_segmenting_label_empty(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table
    sel = st.select_by_segmenting(f, length=16.0, annotations=a, step=4.0, keep_only_empty=True, label_empty=6, pad=False)
    # check selection table
    d = '''filename sel_id start end label
f0.wav   2         8.0  24.0  6
f0.wav   3        12.0  28.0  6
f1.wav   2         8.0  24.0  6
f1.wav   3        12.0  28.0  6
f2.wav   3        12.0  28.0  6
f2.wav   4        16.0  32.0  6
f3.wav   0         0.0  16.0  6
f3.wav   1         4.0  20.0  6
f3.wav   2         8.0  24.0  6
f3.wav   3        12.0  28.0  6
f3.wav   4        16.0  32.0  6
f4.wav   0         0.0  16.0  6
f4.wav   1         4.0  20.0  6
f4.wav   2         8.0  24.0  6
f4.wav   3        12.0  28.0  6
f4.wav   4        16.0  32.0  6
f5.wav   0         0.0  16.0  6
f5.wav   1         4.0  20.0  6
f5.wav   2         8.0  24.0  6
f5.wav   3        12.0  28.0  6
f5.wav   4        16.0  32.0  6'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, sel[ans.columns.values])


def test_select_by_segmenting_avoid_label(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table[:2]
    sel, _ = st.select_by_segmenting(f, length=16.0, annotations=a, step=4.0, avoid_label=[2], pad=False)
    # check selection table
    d = '''filename sel_id start end
f0.wav   1         4.0  20.0
f0.wav   2         8.0  24.0
f0.wav   3        12.0  28.0
f1.wav   0         0.0  16.0
f1.wav   1         4.0  20.0
f1.wav   2         8.0  24.0
f1.wav   3        12.0  28.0'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(ans, sel[ans.columns.values])


def test_query_labeled(annot_table_std):
    df = st.standardize(annot_table_std)
    df = st.select(df, length=1, center=True)
    # query for file that does not exist
    q = st.query_labeled(df, filename='fff.wav')
    assert len(q) == 0
    # query for 1 file
    q = st.query_labeled(df, filename='f1.wav')
    d = '''filename sel_id label  start   end                   
f1.wav  0           3   2.15  3.15
f1.wav  1           1   5.15  6.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(q, ans[q.columns.values])
    # query for 1 file, and 1 that does not exist
    q = st.query_labeled(df, filename=['f1.wav','fff.wav'])
    d = '''filename sel_id label  start   end                   
f1.wav   0           3   2.15  3.15
f1.wav   1           1   5.15  6.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(q, ans[q.columns.values])
    # query for 2 files
    q = st.query_labeled(df, filename=['f1.wav','f2.wav'])
    d = '''filename sel_id label  start   end                            
f1.wav   0           3   2.15  3.15
f1.wav   1           1   5.15  6.15
f2.wav   0           4   3.15  4.15
f2.wav   1           0   6.15  7.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(q, ans[q.columns.values])
    # query for labels
    q = st.query_labeled(df, label=[1,4])
    d = '''filename sel_id label  start   end                   
f0.wav   1           1   4.15  5.15
f1.wav   1           1   5.15  6.15
f2.wav   0           4   3.15  4.15'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(q, ans[q.columns.values])
    # query for label that does not exist
    q = st.query_labeled(df, label=99)
    assert len(q) == 0


def test_query_annotated(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table
    sel = st.select_by_segmenting(f, length=5.1, annotations=a, step=4.0, discard_empty=True, pad=True)
    # query for 1 file
    q1, q2 = st.query_annotated(sel[0], sel[1], label=[1,3])
    d = '''filename sel_id start  end
f0.wav   0         0.0  5.1
f0.wav   1         4.0  9.1
f1.wav   0         0.0  5.1
f1.wav   1         4.0  9.1'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1])
    pd.testing.assert_frame_equal(q1, ans[q1.columns.values])
    d = '''filename sel_id annot_id label  start  end  
f0.wav   0      1             1    3.0  6.3
f0.wav   1      1             1   -1.0  2.3
f1.wav   0      0             3    1.0  4.3
f1.wav   0      1             1    4.0  7.3
f1.wav   1      0             3   -3.0  0.3
f1.wav   1      1             1    0.0  3.3'''
    ans = pd.read_csv(StringIO(d), delim_whitespace=True, index_col=[0,1,2])
    pd.testing.assert_frame_equal(q2, ans[q2.columns.values])


def test_file_duration_table(five_time_stamped_wave_files):
    """ Test that we can generate a file duration table""" 
    df = st.file_duration_table(five_time_stamped_wave_files)
    d = '''filename,duration
empty_HMS_12_ 5_ 0__DMY_23_ 2_84.wav,0.5
empty_HMS_12_ 5_ 1__DMY_23_ 2_84.wav,0.5
empty_HMS_12_ 5_ 2__DMY_23_ 2_84.wav,0.5
empty_HMS_12_ 5_ 3__DMY_23_ 2_84.wav,0.5
empty_HMS_12_ 5_ 4__DMY_23_ 2_84.wav,0.5'''
    ans = pd.read_csv(StringIO(d))
    pd.testing.assert_frame_equal(df, ans[df.columns.values])

def test_file_duration_table_datetime(five_time_stamped_wave_files):
    """ Test that we can generate a file duration table with datetime column""" 
    df = st.file_duration_table(five_time_stamped_wave_files, datetime_format="*HMS_%H_%M_%S__DMY_%d_%m_%y.wav")
    d = '''filename,duration,datetime
empty_HMS_12_ 5_ 0__DMY_23_ 2_84.wav,0.5,1984-02-23 12:05:00
empty_HMS_12_ 5_ 1__DMY_23_ 2_84.wav,0.5,1984-02-23 12:05:01
empty_HMS_12_ 5_ 2__DMY_23_ 2_84.wav,0.5,1984-02-23 12:05:02
empty_HMS_12_ 5_ 3__DMY_23_ 2_84.wav,0.5,1984-02-23 12:05:03
empty_HMS_12_ 5_ 4__DMY_23_ 2_84.wav,0.5,1984-02-23 12:05:04'''
    ans = pd.read_csv(StringIO(d)).astype({'datetime':np.datetime64})
    pd.testing.assert_frame_equal(df, ans[df.columns.values])


def test_random_choice(annot_table_std, file_duration_table):
    a = st.standardize(annot_table_std)
    f = file_duration_table
    sel = st.select_by_segmenting(f, length=16.0, annotations=a, step=4.0, keep_only_empty=True, pad=False)
    sel = st.random_choice(sel, siz=3)
    assert len(sel) == 3
    a = st.random_choice(a, siz=2)
    assert len(a) == 2


def test_aggregate_duration(annot_table_std):
    df = st.standardize(annot_table_std)
    agg_dur = st.aggregate_duration(df)
    assert agg_dur == 18.9
    agg_dur = st.aggregate_duration(df, label=1)
    assert agg_dur == 6.6