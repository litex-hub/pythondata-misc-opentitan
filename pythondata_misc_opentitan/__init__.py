import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5356"
version_tuple = (0, 0, 5356)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5356")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5261"
data_version_tuple = (0, 0, 5261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5261")
except ImportError:
    pass
data_git_hash = "fa58e85f97f67ec6ba3435ede5a5d31949dd06c0"
data_git_describe = "v0.0-5261-gfa58e85f9"
data_git_msg = """\
commit fa58e85f97f67ec6ba3435ede5a5d31949dd06c0
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 11 12:00:03 2021 -0800

    [rbox] update hjson to use bus_interfaces
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
