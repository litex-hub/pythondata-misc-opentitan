import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10306"
version_tuple = (0, 0, 10306)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10306")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10180"
data_version_tuple = (0, 0, 10180)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10180")
except ImportError:
    pass
data_git_hash = "f6a2774f0636997d524d44680eb185f10cec74ab"
data_git_describe = "v0.0-10180-gf6a2774f0"
data_git_msg = """\
commit f6a2774f0636997d524d44680eb185f10cec74ab
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Feb 10 17:59:56 2022 +0100

    [aes] Use prim_sec_anchor_buf for signals relevant for status tracking
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
