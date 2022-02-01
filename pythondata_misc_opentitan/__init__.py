import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9978"
version_tuple = (0, 0, 9978)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9978")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9854"
data_version_tuple = (0, 0, 9854)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9854")
except ImportError:
    pass
data_git_hash = "349cc4dc7d867e3d4cbaf1ad819bbfaa961b2d0a"
data_git_describe = "v0.0-9854-g349cc4dc7"
data_git_msg = """\
commit 349cc4dc7d867e3d4cbaf1ad819bbfaa961b2d0a
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Feb 1 11:44:27 2022 -0800

    [dv/reggen] Fix xcelium hdl backdoor path error
    
    When reggen tool set the following entities:
    1). set_hdl_path_root("tb.dut", "BkdrRegPathRtl");
    2).       alert_test.add_hdl_path_slice(
              ".u_reg.u_alert_test_recov_ctrl_update_err.qs",
              0, 1, 0, "BkdrRegPathRtl");
    Xcelium will add another `.` while forming the hdl path.
    This PR removes the extra `.` in front of `u_reg` to avoid xcelilum
    hdl path error.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
