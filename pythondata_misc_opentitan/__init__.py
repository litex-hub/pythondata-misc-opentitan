import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14756"
version_tuple = (0, 0, 14756)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14756")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14614"
data_version_tuple = (0, 0, 14614)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14614")
except ImportError:
    pass
data_git_hash = "045f122c7138a184b4789fa85d4df62a9a1515e9"
data_git_describe = "v0.0-14614-g045f122c71"
data_git_msg = """\
commit 045f122c7138a184b4789fa85d4df62a9a1515e9
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 13 11:38:04 2022 -0700

    [spi_device/dv] Update coverage plan and implement covergroup
    
    1. Largely updated the coverage plan
    2. Implemented covergroup for fw and tpm mode. Will add for flash mode
    in the next PR
    3. Add 2 more tests in testplan - stress all and
    tpm_and_flash_trans_with_min_inactive_time
    
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
