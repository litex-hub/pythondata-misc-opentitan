import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12497"
version_tuple = (0, 0, 12497)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12497")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12355"
data_version_tuple = (0, 0, 12355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12355")
except ImportError:
    pass
data_git_hash = "68d279f2ee522997f7e321b29b91576cd621459c"
data_git_describe = "v0.0-12355-g68d279f2e"
data_git_msg = """\
commit 68d279f2ee522997f7e321b29b91576cd621459c
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jun 2 16:33:40 2022 -0700

    chore(cdc): Waive W_GLITCH for pads input to sync
    
    This commit waives the W_GLITCH errors on the path from PADs input to
    any 2FF sync cells.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
