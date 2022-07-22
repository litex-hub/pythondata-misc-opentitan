import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13250"
version_tuple = (0, 0, 13250)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13250")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13108"
data_version_tuple = (0, 0, 13108)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13108")
except ImportError:
    pass
data_git_hash = "95ae6de7a59d44fe55f49857cf7bc2878b400cfc"
data_git_describe = "v0.0-13108-g95ae6de7a5"
data_git_msg = """\
commit 95ae6de7a59d44fe55f49857cf7bc2878b400cfc
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jul 19 14:25:57 2022 -0700

    [dv/rstmgr] Fix sec_cm_scan_intersig_mubi failure
    
    Block wiggling scanmode_i while scan_rst_ni is active, or the smoke
    sequence will fail to generate a scan reset, and fail.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
