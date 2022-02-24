import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10520"
version_tuple = (0, 0, 10520)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10520")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10394"
data_version_tuple = (0, 0, 10394)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10394")
except ImportError:
    pass
data_git_hash = "049c47288cfd48548b9afa80091e9774dc5dc721"
data_git_describe = "v0.0-10394-g049c47288"
data_git_msg = """\
commit 049c47288cfd48548b9afa80091e9774dc5dc721
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 22 10:44:52 2022 +0100

    [fpga, clkmgr] Use global clock buffer for KMAC
    
    KMAC keeps growing in size, especially with masking turned on it barely
    fits a single clock region. For this reason, this commit uses a global
    clock buffer for KMAC to give Vivado more freedom in placing and routing
    KMAC.
    
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
