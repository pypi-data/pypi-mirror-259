@echo off
call conda activate py38
pip install taichi pybind11 pefile machomachomangler
python setup.py bdist_wheel
python scripts\win\win_auto_repair.py --py 38 --version 0.2.7
