import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10786"
version_tuple = (0, 0, 10786)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10786")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10660"
data_version_tuple = (0, 0, 10660)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10660")
except ImportError:
    pass
data_git_hash = "09ef94e1a7a3f8d99854537f2e201b219e39fefc"
data_git_describe = "v0.0-10660-g09ef94e1a"
data_git_msg = """\
commit 09ef94e1a7a3f8d99854537f2e201b219e39fefc
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Mar 7 15:39:22 2022 -0800

    Fix UART timeout issues
    
    1. Fix timeout detection for the verilator UART.
    2. Add timeout detection for the common-case UART.
    3. Print backtraces if available.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
