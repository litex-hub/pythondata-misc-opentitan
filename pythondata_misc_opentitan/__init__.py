import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5770"
version_tuple = (0, 0, 5770)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5770")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5675"
data_version_tuple = (0, 0, 5675)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5675")
except ImportError:
    pass
data_git_hash = "da747944e586427d3e8cd316a85d90febc01e211"
data_git_describe = "v0.0-5675-gda747944e"
data_git_msg = """\
commit da747944e586427d3e8cd316a85d90febc01e211
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Apr 8 07:49:48 2021 +0100

    [rom_ctrl] Hook up the other bus integrity error signals in rom_ctrl
    
    It seems that I managed one register top but not the other one, or the
    SRAM adapter. Oops!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
