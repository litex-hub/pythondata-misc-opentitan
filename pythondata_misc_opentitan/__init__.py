import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8824"
version_tuple = (0, 0, 8824)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8824")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8712"
data_version_tuple = (0, 0, 8712)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8712")
except ImportError:
    pass
data_git_hash = "41b2628d1ad68a7c80073e00ddd5889278b38686"
data_git_describe = "v0.0-8712-g41b2628d1"
data_git_msg = """\
commit 41b2628d1ad68a7c80073e00ddd5889278b38686
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Nov 11 16:32:51 2021 -0800

    [pwrmgr] Make rom_ctrl check signals multi-bit
    
    - This fixes #8981 but only addresses the issue on pwrmgr side.
    - rom_ctrl may be further enhanced.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
