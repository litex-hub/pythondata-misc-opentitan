import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5738"
version_tuple = (0, 0, 5738)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5738")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5643"
data_version_tuple = (0, 0, 5643)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5643")
except ImportError:
    pass
data_git_hash = "71174e0585ac0611566754b28a303b21faaba700"
data_git_describe = "v0.0-5643-g71174e058"
data_git_msg = """\
commit 71174e0585ac0611566754b28a303b21faaba700
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Apr 5 16:17:29 2021 -0700

    [dv/otp_ctrl] stress_all_with_rand_reset test part 1
    
    This PR clears up stress_all_with_rand_reset test compile issues.
    1. Fix the constraint names that does not match the base constraint name
    2. Clean up cfg.hjson and testplan
    3. Turn on the access mode for test_access region, so tl_error in
    stress_all_with_reset sequence won't hang
    
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
