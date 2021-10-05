import subprocess
import sys

import pytest


def speedoc(*args):
    subprocess.check_call([sys.executable, "-m_speedoc", *args])


def test_main():
    speedoc("sphinx")
    speedoc("sphinx.__version__")
    with pytest.raises(subprocess.CalledProcessError):
        speedoc("sphinx", "sphinx.__version__")
