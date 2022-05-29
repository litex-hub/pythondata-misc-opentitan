import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12400"
version_tuple = (0, 0, 12400)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12400")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12260"
data_version_tuple = (0, 0, 12260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12260")
except ImportError:
    pass
data_git_hash = "0b8904a6d73abb99581a982be3c3f7f64bbd3b8c"
data_git_describe = "v0.0-12260-g0b8904a6d"
data_git_msg = """\
commit 0b8904a6d73abb99581a982be3c3f7f64bbd3b8c
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu May 26 07:08:09 2022 -0700

    [prim_assert] Fix ASSERT_FPV_LINEAR_FSM
    
    This assertion should handle an lc reset, even though the reset and idle
    states will be revisited.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
