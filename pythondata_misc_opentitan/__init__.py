import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5616"
version_tuple = (0, 0, 5616)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5616")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5521"
data_version_tuple = (0, 0, 5521)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5521")
except ImportError:
    pass
data_git_hash = "fb12cc291fe0328250ac69d6484649cd5f2c54a1"
data_git_describe = "v0.0-5521-gfb12cc291"
data_git_msg = """\
commit fb12cc291fe0328250ac69d6484649cd5f2c54a1
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Mar 25 14:14:42 2021 -0700

    [dv/otp_ctrl] fix regression otp ecc error
    
    This PR fixes regression ECC error. If there is an ACCESS ERROR, OTP
    won't detect ECC error because the read is blocked.
    
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
