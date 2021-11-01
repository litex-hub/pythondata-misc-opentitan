import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8554"
version_tuple = (0, 0, 8554)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8554")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8442"
data_version_tuple = (0, 0, 8442)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8442")
except ImportError:
    pass
data_git_hash = "14910ab11fef319ba5cbf6369d6d5938cb76b29c"
data_git_describe = "v0.0-8442-g14910ab11"
data_git_msg = """\
commit 14910ab11fef319ba5cbf6369d6d5938cb76b29c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Nov 1 10:23:58 2021 -0700

    [dv/clkmgr rstmgr] Fix post_apply_reset issue
    
    This PR fixes the regression error where tl_integrity error failed on
    both clkmgr and rstmgr.
    The reason is that `post_apply_reset` task did not call super task.
    This PR also removes dut_init in cip_base_vseq as there is nothing to
    override.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
