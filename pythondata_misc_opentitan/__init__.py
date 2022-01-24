import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9716"
version_tuple = (0, 0, 9716)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9716")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9594"
data_version_tuple = (0, 0, 9594)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9594")
except ImportError:
    pass
data_git_hash = "3bda020dda70d422e115535e29fdf99cc1f6e86f"
data_git_describe = "v0.0-9594-g3bda020dd"
data_git_msg = """\
commit 3bda020dda70d422e115535e29fdf99cc1f6e86f
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jan 21 22:48:21 2022 -0800

    [doc] Add D2S as valid entry in dashboard script
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
