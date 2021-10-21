import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8384"
version_tuple = (0, 0, 8384)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8384")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8272"
data_version_tuple = (0, 0, 8272)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8272")
except ImportError:
    pass
data_git_hash = "45faebcae0fcbf5c34d2d8fbc49869d95af60bb8"
data_git_describe = "v0.0-8272-g45faebcae"
data_git_msg = """\
commit 45faebcae0fcbf5c34d2d8fbc49869d95af60bb8
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 20 16:13:41 2021 -0700

    [opentitantool] Run `cargo fmt`
    
    1. Apply standard formatting via `cargo fmt`.
    
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
