import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10103"
version_tuple = (0, 0, 10103)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10103")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9979"
data_version_tuple = (0, 0, 9979)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9979")
except ImportError:
    pass
data_git_hash = "2babd940e9b65794cabd1351c112e7b016475d57"
data_git_describe = "v0.0-9979-g2babd940e"
data_git_msg = """\
commit 2babd940e9b65794cabd1351c112e7b016475d57
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Feb 4 20:19:18 2022 -0800

    [sysrst_ctrl] Add some more details regarding combo actions
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
