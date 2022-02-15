import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10321"
version_tuple = (0, 0, 10321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10195"
data_version_tuple = (0, 0, 10195)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10195")
except ImportError:
    pass
data_git_hash = "424a57d046d85e9cc854c63167d966d7558ccbf9"
data_git_describe = "v0.0-10195-g424a57d04"
data_git_msg = """\
commit 424a57d046d85e9cc854c63167d966d7558ccbf9
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Feb 15 16:33:00 2022 +0000

    [ci] Move Verilator build to ci-public pool
    
    Previously this used azure agents, which are slow. Using ci-public
    should improve the speed of the verilator build.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
