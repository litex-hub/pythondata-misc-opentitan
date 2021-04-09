import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5794"
version_tuple = (0, 0, 5794)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5794")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5699"
data_version_tuple = (0, 0, 5699)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5699")
except ImportError:
    pass
data_git_hash = "7571540532f42d5371f312b4e0443a5a70b1034e"
data_git_describe = "v0.0-5699-g757154053"
data_git_msg = """\
commit 7571540532f42d5371f312b4e0443a5a70b1034e
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Apr 8 17:01:24 2021 -0700

    [dv/otp_ctrl] Fix regression stress_all_with_reset error
    
    This PR fixes two errors in stress_all_with_reset test:
    1. Constraint conflict: I will disable this constriant when
    stress_all_with_reset test is running.
    
    2. When reset is issued during OTP write, the scb cannot accurately
    predict how much writing has OTP memory done. So the plan is to backdoor
    read back the specific address after reset is issued.
    
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
