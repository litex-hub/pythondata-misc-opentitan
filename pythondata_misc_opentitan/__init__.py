import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5638"
version_tuple = (0, 0, 5638)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5638")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5543"
data_version_tuple = (0, 0, 5543)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5543")
except ImportError:
    pass
data_git_hash = "5f6bc725d60d2d1cdc7c7eb592e6f3d5eb064126"
data_git_describe = "v0.0-5543-g5f6bc725d"
data_git_msg = """\
commit 5f6bc725d60d2d1cdc7c7eb592e6f3d5eb064126
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 29 21:20:47 2021 -0700

    [dv/otp_ctrl] fix lc_esc_req regression failure
    
    This PR fixes lc_esc_req regression failure.
    Current issue:
    If reset is issued during lc_prog_req, scb cannot predict how many OTP
    memory cells have been programmed.
    
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
