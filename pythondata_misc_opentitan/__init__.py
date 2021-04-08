import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5764"
version_tuple = (0, 0, 5764)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5764")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5669"
data_version_tuple = (0, 0, 5669)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5669")
except ImportError:
    pass
data_git_hash = "05ef653345ee6b8eb7cb8fc13df22e499c511d1d"
data_git_describe = "v0.0-5669-g05ef65334"
data_git_msg = """\
commit 05ef653345ee6b8eb7cb8fc13df22e499c511d1d
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Apr 7 15:20:30 2021 -0700

    [otp_ctrl] fix compile error
    
    TLUL port `req_type_o` was declared twice and has a compile error.
    This PR fixes it.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
