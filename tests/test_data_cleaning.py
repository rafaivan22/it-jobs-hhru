import subprocess
import sys

def test_data_cleaning_runs():
    result = subprocess.run([sys.executable, "scripts/data_cleaning.py"], capture_output=True)
    assert result.returncode == 0
