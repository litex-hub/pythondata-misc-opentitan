import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11488"
version_tuple = (0, 0, 11488)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11488")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11362"
data_version_tuple = (0, 0, 11362)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11362")
except ImportError:
    pass
data_git_hash = "375f4fd479d1392a6d2be219384f49f8159cf20f"
data_git_describe = "v0.0-11362-g375f4fd47"
data_git_msg = """\
commit 375f4fd479d1392a6d2be219384f49f8159cf20f
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Wed Apr 6 14:27:43 2022 +0000

    dv,top,rstmgr] chip_sw_rstrmgr_sw_rst
    
       1. This test checks rstmgr.sw_rst_ctrl_n[] with peripheral devices.
       2. fix typo in chip_testplan reset manager section
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
