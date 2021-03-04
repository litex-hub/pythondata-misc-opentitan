import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5249"
version_tuple = (0, 0, 5249)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5249")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5158"
data_version_tuple = (0, 0, 5158)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5158")
except ImportError:
    pass
data_git_hash = "f2cc96330c0ac7a53f966fa7b3e32419207384f5"
data_git_describe = "v0.0-5158-gf2cc96330"
data_git_msg = """\
commit f2cc96330c0ac7a53f966fa7b3e32419207384f5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Mar 4 09:15:41 2021 -0800

    [alert_handler] Delete stale comment
    
    Fix #5457
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
