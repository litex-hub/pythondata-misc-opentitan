import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15247"
version_tuple = (0, 0, 15247)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15247")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15105"
data_version_tuple = (0, 0, 15105)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15105")
except ImportError:
    pass
data_git_hash = "fb80b7ab8909c8f9d45683c77258624e986a28b3"
data_git_describe = "v0.0-15105-gfb80b7ab89"
data_git_msg = """\
commit fb80b7ab8909c8f9d45683c77258624e986a28b3
Author: Weicai Yang <weicai@google.com>
Date:   Thu Nov 3 14:55:40 2022 -0700

    [dv] Skip checking alert if scb is disabled
    
    scb may be disabled in the middle of sim. Check if scb is off before firing an error.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
