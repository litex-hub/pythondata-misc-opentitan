import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5847"
version_tuple = (0, 0, 5847)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5847")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5752"
data_version_tuple = (0, 0, 5752)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5752")
except ImportError:
    pass
data_git_hash = "aa96b51e9a70e92051fd3a15b9b1567a74c5d8a8"
data_git_describe = "v0.0-5752-gaa96b51e9"
data_git_msg = """\
commit aa96b51e9a70e92051fd3a15b9b1567a74c5d8a8
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Apr 9 22:12:25 2021 -0700

    [dv/otp_ctrl] Fix regression lc output mismatch
    
    This PR fixes three lc_esc related mismatch:
    1). when lc_esc is On, the otp_lc_o should return default value.
    2). when lc_esc is issued during otp write, it will wait until OTP write
    complete, then backdoor align
    3). when reset/lc_esc_on is issued during digest calculate, will use
    backdoor to recover digest value.
    
    This PR also adds lc_esc_en sequence to stress_all test.
    
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
