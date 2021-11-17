import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8746"
version_tuple = (0, 0, 8746)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8746")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8634"
data_version_tuple = (0, 0, 8634)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8634")
except ImportError:
    pass
data_git_hash = "a601c7a6ca50b8e53800ba89c3f13b17d3271db0"
data_git_describe = "v0.0-8634-ga601c7a6c"
data_git_msg = """\
commit a601c7a6ca50b8e53800ba89c3f13b17d3271db0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Nov 11 09:28:22 2021 -0800

    [fpv] Fix compile warning regarding types
    
    The output type of prim_mubi_sync is an array of mubis, so we change the
    output signal to an array of size 1.
    
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
