import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5576"
version_tuple = (0, 0, 5576)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5576")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5481"
data_version_tuple = (0, 0, 5481)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5481")
except ImportError:
    pass
data_git_hash = "e390f206647af8a380cfaa406b157deca6f3e78b"
data_git_describe = "v0.0-5481-ge390f2066"
data_git_msg = """\
commit e390f206647af8a380cfaa406b157deca6f3e78b
Author: Cindy Chen <chencindy@google.com>
Date:   Wed Mar 24 13:00:52 2021 -0700

    [dv/otp_ctrl] Add back tlul error data check
    
    This PR is based on PR #5784 that design will always return d_data as 0
    when d_error occurred in tlul memory read.
    This PR also:
    1. add more possiblilities to hit the TLUL sw partition memory error
    case
    2. include digest address in tlul memory error check
    
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
