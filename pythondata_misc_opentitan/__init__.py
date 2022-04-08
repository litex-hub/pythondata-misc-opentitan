import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11479"
version_tuple = (0, 0, 11479)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11479")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11353"
data_version_tuple = (0, 0, 11353)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11353")
except ImportError:
    pass
data_git_hash = "06ccc1ea1828d78b5a9651ab3c6d4e7480a6b541"
data_git_describe = "v0.0-11353-g06ccc1ea1"
data_git_msg = """\
commit 06ccc1ea1828d78b5a9651ab3c6d4e7480a6b541
Author: Michael Schaffner <msf@google.com>
Date:   Thu Apr 7 19:11:49 2022 -0700

    [tlul_lc_gate] Use prim_blanker instead of muxes and buffers
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
