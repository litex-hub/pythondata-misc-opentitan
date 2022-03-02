import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10642"
version_tuple = (0, 0, 10642)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10642")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10516"
data_version_tuple = (0, 0, 10516)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10516")
except ImportError:
    pass
data_git_hash = "52fdb718f4c91640caf0f1fe31282b1c79d3e921"
data_git_describe = "v0.0-10516-g52fdb718f"
data_git_msg = """\
commit 52fdb718f4c91640caf0f1fe31282b1c79d3e921
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 1 14:52:09 2022 -0800

    [dv/otp_ctrl] Further reduce otp smoke test iteration to avoid timeout
    
    This PR futher reduces OTP_CTRL smoke test runtime, because in close
    source it takes a long time to simulate OTP read/write.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
