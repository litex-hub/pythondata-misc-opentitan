import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15136"
version_tuple = (0, 0, 15136)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15136")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14994"
data_version_tuple = (0, 0, 14994)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14994")
except ImportError:
    pass
data_git_hash = "8e7f2778a4277a5854a0843850b812e8363e0b45"
data_git_describe = "v0.0-14994-g8e7f2778a4"
data_git_msg = """\
commit 8e7f2778a4277a5854a0843850b812e8363e0b45
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Nov 1 17:10:13 2022 -0700

    [rust] Update to serde-annotate v0.0.5
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
