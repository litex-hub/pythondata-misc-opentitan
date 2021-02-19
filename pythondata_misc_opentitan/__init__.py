import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5047"
version_tuple = (0, 0, 5047)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5047")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4956"
data_version_tuple = (0, 0, 4956)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4956")
except ImportError:
    pass
data_git_hash = "771d397f79a0fc80d9cc36bb003fc06fabdccb97"
data_git_describe = "v0.0-4956-g771d397f7"
data_git_msg = """\
commit 771d397f79a0fc80d9cc36bb003fc06fabdccb97
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Feb 12 16:39:37 2021 -0800

    [dv/otp_ctrl] update regwen access policy
    
    This PR follows the change from `W1C` to `W0C`, so we change the random
    distribution to follow the change.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
