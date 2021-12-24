import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9293"
version_tuple = (0, 0, 9293)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9293")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9176"
data_version_tuple = (0, 0, 9176)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9176")
except ImportError:
    pass
data_git_hash = "478730670dbe2a0342fbee7062dde7e7e7cc447d"
data_git_describe = "v0.0-9176-g478730670"
data_git_msg = """\
commit 478730670dbe2a0342fbee7062dde7e7e7cc447d
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Dec 23 08:31:23 2021 -0800

    [top] Switch USB pads to new dual pad type
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
