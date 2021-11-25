import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8863"
version_tuple = (0, 0, 8863)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8863")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8751"
data_version_tuple = (0, 0, 8751)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8751")
except ImportError:
    pass
data_git_hash = "515307e08511df8545bea5596a3df525fd3c546a"
data_git_describe = "v0.0-8751-g515307e08"
data_git_msg = """\
commit 515307e08511df8545bea5596a3df525fd3c546a
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Nov 19 14:05:41 2021 +0000

    [prim] Fix prim_ram_1p_scr Dependencies
    
    This commit includes addition of necessary primitives to the
    `.core` file prim_ram_1p_scr and removing prim:all dependency.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
