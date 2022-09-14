import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14195"
version_tuple = (0, 0, 14195)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14195")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14053"
data_version_tuple = (0, 0, 14053)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14053")
except ImportError:
    pass
data_git_hash = "85600eec69b9c79423fbb93a3b186f3e953ca729"
data_git_describe = "v0.0-14053-g85600eec69"
data_git_msg = """\
commit 85600eec69b9c79423fbb93a3b186f3e953ca729
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Sep 13 16:24:15 2022 -0700

    [dv/otp_ctrl] Sec_cm test update
    
    This PR update otp_ctrl_sec_cm test after design moves prim_otp alerts
    to the OTP_CTRL standard wrappers.
    With this movement, we need to slightly change the testbench because:
    1). prim_otp module output to a separate alerts.
    2). prim_otp module's alert only bypass OTP_CTRL, it does not create any
      actual error.
    3). tl_integrity error coming from prim_otp module will only bypass
      OTP_CTRL as well.
    4). LC_gate module will output to a different alert output.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
