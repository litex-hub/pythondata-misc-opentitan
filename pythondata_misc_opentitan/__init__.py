import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10244"
version_tuple = (0, 0, 10244)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10244")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10120"
data_version_tuple = (0, 0, 10120)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10120")
except ImportError:
    pass
data_git_hash = "5fbb8f72677bf48ef034222a514913c09ce61c6e"
data_git_describe = "v0.0-10120-g5fbb8f726"
data_git_msg = """\
commit 5fbb8f72677bf48ef034222a514913c09ce61c6e
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Thu Feb 10 09:58:16 2022 +0000

    [lc_ctrl/dv] Addressed comments in #10246
    
    - Deleted lc_ctrl_cov_if.sv:
    https://github.com/lowRISC/opentitan/pull/10246#discussion_r802079172
    - Updated type of otp_vendor_test_ctrl and otp_vendor_test_status in lc_ctrl_env_cfg.sv:
    https://github.com/lowRISC/opentitan/pull/10246#discussion_r802082681
    - Updated error message to UVM_MEDIUM:
    https://github.com/lowRISC/opentitan/pull/10246#discussion_r802084957
    - Added back port toggle coverage for RV_TAP:
    https://github.com/lowRISC/opentitan/pull/10246#discussion_r803431294
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
