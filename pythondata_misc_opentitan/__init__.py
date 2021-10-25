import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8429"
version_tuple = (0, 0, 8429)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8429")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8317"
data_version_tuple = (0, 0, 8317)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8317")
except ImportError:
    pass
data_git_hash = "957b7de0ffaa0bef5d6614b123f5671cac5aa4b6"
data_git_describe = "v0.0-8317-g957b7de0f"
data_git_msg = """\
commit 957b7de0ffaa0bef5d6614b123f5671cac5aa4b6
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Oct 21 16:01:29 2021 +0100

    [sw] Adjust build logic in ECDSA-P256 for crypto library.
    
    Move some universal definitions to the top-level crypto library build
    file, and rename variables for better readability.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
