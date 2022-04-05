import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11367"
version_tuple = (0, 0, 11367)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11367")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11241"
data_version_tuple = (0, 0, 11241)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11241")
except ImportError:
    pass
data_git_hash = "a01a0cc9621247b40b2a149154496f5cf7377e4d"
data_git_describe = "v0.0-11241-ga01a0cc96"
data_git_msg = """\
commit a01a0cc9621247b40b2a149154496f5cf7377e4d
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Apr 5 01:51:07 2022 +0000

    [dv,pwrmgr] fix regression failure
    
     - pwrmgr_sec_cm_lc_ctrl_intersig_mubi : disalbe assertion
    
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
