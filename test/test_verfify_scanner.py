import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from antivirus.antivirus import check_lines


def test_normal_scripts():
    # arrange test by set path of folder
    current_path = os.path.abspath(os.path.dirname(__file__))
    resource_path = os.path.join(current_path, 'resources/normal')
    # act test by analysing file
    count = 0
    for path, subdirs, files in os.walk(resource_path):
        for name in files:
            filename = os.path.join(path, name)
            with open(filename, 'r') as f:
                if not check_lines(f.readlines()):
                    count += 1
    # assert count of detected issues
    assert count == 0


def test_viruses():
    # arrange test by set path of folder
    current_path = os.path.abspath(os.path.dirname(__file__))
    resource_path = os.path.join(current_path, 'resources/viruses')
    # act test by analysing file
    count = 0
    for path, subdirs, files in os.walk(resource_path):
        for name in files:
            filename = os.path.join(path, name)
            with open(filename, 'r') as f:
                if not check_lines(f.readlines()):
                    count += 1
    # assert count of detected issues
    assert count == 2
