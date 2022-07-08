import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13001"
version_tuple = (0, 0, 13001)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13001")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12859"
data_version_tuple = (0, 0, 12859)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12859")
except ImportError:
    pass
data_git_hash = "1a180062f29790d404cf1d363fc27eca4af99c3e"
data_git_describe = "v0.0-12859-g1a180062f2"
data_git_msg = """\
commit 1a180062f29790d404cf1d363fc27eca4af99c3e
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jul 8 12:37:50 2022 -0700

    [alert_handler] Align docs for crashdump latching
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
