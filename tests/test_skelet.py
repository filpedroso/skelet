import time
import os
from unittest.mock import patch
from lib_skelet import pics_list
from interface_skelet import loadfile, timed_display


@patch('builtins.print')
@patch('time.sleep')
@patch('os.system')
def test_timed_display(mock_os, mock_sleep, mock_print):

    # mocks whether the functions were called at least once with the correct inputs
    text = "Hello, World!"
    duration = 2
    timed_display(text, duration)   
    mock_print.assert_called_once_with(text)
    mock_sleep.assert_called_once_with(duration)

    # if windows or unix, tests if clear screen was called
    if os.name == 'nt':
        mock_os.assert_called_once_with('cls')
    else:
        mock_os.assert_called_once_with('clear')


@patch('os.path.abspath')
@patch('os.path.dirname')
@patch('os.listdir')
def test_pics_list(mock_listdir, mock_dirname, mock_abspath):

    # creates mock results for each funtion return value
    mock_abspath.return_value = "/mock/path/to/lib_skelet.py"
    mock_dirname.return_value = "/mock/path/to"
    mock_listdir.return_value = ['image1.raw', 'image2.raw', 'image3.raw']

    expected_result = ['image1.raw', 'image2.raw', 'image3.raw']

    result = pics_list()

    # asserts functions were called at least once
    mock_abspath.assert_called_once()
    mock_dirname.assert_called_once_with("/mock/path/to/lib_skelet.py")
    mock_listdir.assert_called_once_with("/mock/path/to/pictures")

    assert result == expected_result


@patch('interface_skelet.tabulate')
def test_loadfile(mock_tabulate):

    # creates input mock list
    pictures = [
        ["image1.raw", "description1"],
        ["image2.raw", "description2"],
        ["image3.raw", "description3"]
    ]

    # mocks output for tabulate
    expected_output = "formatted table"
    mock_tabulate.return_value = expected_output
    
    result = loadfile(pictures)
    
    mock_tabulate.assert_called_once_with(pictures, headers=["picture file", "input this"])
    assert result == expected_output