import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5864"
version_tuple = (0, 0, 5864)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5864")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5769"
data_version_tuple = (0, 0, 5769)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5769")
except ImportError:
    pass
data_git_hash = "d9dc048680d89bd630ffae673103509e28017709"
data_git_describe = "v0.0-5769-gd9dc04868"
data_git_msg = """\
commit d9dc048680d89bd630ffae673103509e28017709
Author: Cindy Chen <chencindy@google.com>
Date:   Sun Apr 11 12:46:21 2021 -0700

    [dv/otp_ctrl] Add background check
    
    This PR adds a single test to check OTP_background checks. This test
    wanted to ensure the background check can be triggered automatically
    once we configured the check periods.
    
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
