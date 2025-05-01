import subprocess
import sys

def test_data_collection_runs():
    result = subprocess.run([sys.executable, "scripts/data_collection.py"], capture_output=True)
    assert result.returncode == 0
