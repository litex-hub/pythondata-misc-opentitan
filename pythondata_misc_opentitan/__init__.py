import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15098"
version_tuple = (0, 0, 15098)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15098")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14956"
data_version_tuple = (0, 0, 14956)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14956")
except ImportError:
    pass
data_git_hash = "11c21b226ecf2add1e7135fb3dac81a3284a29cf"
data_git_describe = "v0.0-14956-g11c21b226e"
data_git_msg = """\
commit 11c21b226ecf2add1e7135fb3dac81a3284a29cf
Author: Fatih Balli <fatihballi@google.com>
Date:   Tue Oct 11 18:15:05 2022 +0200

    [chip_sw, sysrst_ctrl] Test ulp wakeup of sysrst_ctrl
    
    Implements chip_sw_sysrst_ctrl_ulp_z3_wakeup.
    
    Signed-off-by: Fatih Balli <fatihballi@google.com>

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
