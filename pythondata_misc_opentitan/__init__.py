import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11361"
version_tuple = (0, 0, 11361)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11361")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11235"
data_version_tuple = (0, 0, 11235)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11235")
except ImportError:
    pass
data_git_hash = "07206099527e1a373ffdff48b7921293095b4db6"
data_git_describe = "v0.0-11235-g072060995"
data_git_msg = """\
commit 07206099527e1a373ffdff48b7921293095b4db6
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Apr 1 16:07:27 2022 -0700

    [opentitantool] Add timestamps to console output
    
    1. When requested via the `--timestamp` flag, each line of console output
       will include the time that it was emitted.
    
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
