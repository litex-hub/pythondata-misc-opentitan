import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8705"
version_tuple = (0, 0, 8705)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8705")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8593"
data_version_tuple = (0, 0, 8593)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8593")
except ImportError:
    pass
data_git_hash = "1ac30bea3b2502e46137e30794349e5452618bf2"
data_git_describe = "v0.0-8593-g1ac30bea3"
data_git_msg = """\
commit 1ac30bea3b2502e46137e30794349e5452618bf2
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Nov 11 16:33:13 2021 -0800

    [sw, cleanup, opentitantool] Minor code formatting cleanups
    
    1. Run `cargo clippy`.  Heed its advice.
    2. Run `cargo fmt`.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
