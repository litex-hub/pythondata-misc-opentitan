import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8573"
version_tuple = (0, 0, 8573)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8573")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8461"
data_version_tuple = (0, 0, 8461)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8461")
except ImportError:
    pass
data_git_hash = "0d25f96ef96dc33247f25b7ffb93e18f752c5299"
data_git_describe = "v0.0-8461-g0d25f96ef"
data_git_msg = """\
commit 0d25f96ef96dc33247f25b7ffb93e18f752c5299
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 28 14:38:23 2021 -0700

    [dv/alert_handler] Add checking for crashdump_o output
    
    This PR supports checking in scb regarding the crashdumo_o output.
    To avoid a cycle-accurate model, I left a TODO to see how to check
    esc_cnt and alert_accum_count.
    
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
