import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15015"
version_tuple = (0, 0, 15015)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15015")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14873"
data_version_tuple = (0, 0, 14873)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14873")
except ImportError:
    pass
data_git_hash = "5a4e508f3e81e0a17eb7a040f8b439e5de7b5d31"
data_git_describe = "v0.0-14873-g5a4e508f3e"
data_git_msg = """\
commit 5a4e508f3e81e0a17eb7a040f8b439e5de7b5d31
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 27 13:28:04 2022 -0700

    [spi_device/dv] Fix regression issues
    
    This will make most of tests 100% pass, except stress_all
    1. Update constrain for flash_mode, need to check mailbox_en before pick an address
    2. Update scb to fix prediction of flash_status for a corner case that dummy item involves
    3. Fix some regression timeout
    4. Remove dummy item in stress_all as it's added in subseq already
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
