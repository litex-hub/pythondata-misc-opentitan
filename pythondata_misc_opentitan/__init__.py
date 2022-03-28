import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11166"
version_tuple = (0, 0, 11166)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11166")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11040"
data_version_tuple = (0, 0, 11040)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11040")
except ImportError:
    pass
data_git_hash = "88dee60904a8872febccc967f914f6b59e190a4f"
data_git_describe = "v0.0-11040-g88dee6090"
data_git_msg = """\
commit 88dee60904a8872febccc967f914f6b59e190a4f
Author: Kosta Kojdic <kosta.kojdic@ensilica.com>
Date:   Tue Mar 22 12:41:59 2022 +0000

    Scoreboard for passthrough mode
    
    Signed-off-by: Kosta Kojdic <kosta.kojdic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
