import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14746"
version_tuple = (0, 0, 14746)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14746")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14604"
data_version_tuple = (0, 0, 14604)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14604")
except ImportError:
    pass
data_git_hash = "0f9276d84df7cd3286914a12ad45d8df186289ff"
data_git_describe = "v0.0-14604-g0f9276d84d"
data_git_msg = """\
commit 0f9276d84df7cd3286914a12ad45d8df186289ff
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 12 11:16:54 2022 -0700

    [quality] Add a rust formatting check
    
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
