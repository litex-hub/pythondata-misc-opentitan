import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11498"
version_tuple = (0, 0, 11498)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11498")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11372"
data_version_tuple = (0, 0, 11372)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11372")
except ImportError:
    pass
data_git_hash = "493fbbdf68d895b8a736236aa791e0e3bced6044"
data_git_describe = "v0.0-11372-g493fbbdf6"
data_git_msg = """\
commit 493fbbdf68d895b8a736236aa791e0e3bced6044
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Apr 8 12:28:05 2022 -0700

    [bazel, clang] Update to the latest bazel-embedded
    
    1. Downloads resources as http archives (for airgapped builds).
    2. Fixes the compiler configuration to not find the system compiler.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
