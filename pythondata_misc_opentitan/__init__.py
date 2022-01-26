import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9805"
version_tuple = (0, 0, 9805)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9805")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9683"
data_version_tuple = (0, 0, 9683)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9683")
except ImportError:
    pass
data_git_hash = "8db83bd9d4cc01fa6c22e85a7190cf5ace9abe86"
data_git_describe = "v0.0-9683-g8db83bd9d"
data_git_msg = """\
commit 8db83bd9d4cc01fa6c22e85a7190cf5ace9abe86
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Jan 20 09:59:20 2022 +0000

    [rom_ctrl, dv] Fixes regression failure relating to tl accesses
    
    There were false failures relating to assertion that checks that all tl
    accesses before rom check is done are blocked off.
    This commit fixes the assertion by adding an additional check that if
    at all d_valid is asserted before the rom check is completed, d_error also
    must be asserted.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
