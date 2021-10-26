import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8445"
version_tuple = (0, 0, 8445)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8445")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8333"
data_version_tuple = (0, 0, 8333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8333")
except ImportError:
    pass
data_git_hash = "3400408d95acfc5852285e1b91914773b674520c"
data_git_describe = "v0.0-8333-g3400408d9"
data_git_msg = """\
commit 3400408d95acfc5852285e1b91914773b674520c
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 25 15:32:42 2021 -0700

    [dv] Move alert init to post_apply_reset
    
    This is needed for stess_all with rand reset, which invokes apply_resets_concurrently
    and post_apply_reset.
    This will also fix uart regression failures
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
