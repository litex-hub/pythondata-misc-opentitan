import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14692"
version_tuple = (0, 0, 14692)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14692")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14550"
data_version_tuple = (0, 0, 14550)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14550")
except ImportError:
    pass
data_git_hash = "1752a8bd6035ff367837cb6bb9ec69a6098e8c62"
data_git_describe = "v0.0-14550-g1752a8bd60"
data_git_msg = """\
commit 1752a8bd6035ff367837cb6bb9ec69a6098e8c62
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Oct 11 16:18:46 2022 -0700

    [dv/otp_ctrl] Fix tl_intg_error nightly failure
    
    This PR fixes the TL_intg_error failure in nightly regression.
    The issue is that: the prim_otp_tl interface does not set any err_code,
    only triggers a prim_otp_alert.
    And the tl_intg_err task is share for sec_cm one_hot check and
    tl_intg_error check.
    
    So we need to distinguish which tlul interface has integrity and sec_cm
    error.
    Because these two tests have different input: ral_name and proxy_path,
    so otp_ctrl_common_vseq create an internal flag to store which tlul
    interface is used.
    
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
