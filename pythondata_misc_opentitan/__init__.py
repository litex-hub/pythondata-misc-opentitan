import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9676"
version_tuple = (0, 0, 9676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9554"
data_version_tuple = (0, 0, 9554)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9554")
except ImportError:
    pass
data_git_hash = "862155839d7ff9b26c5515b49717a34554997b73"
data_git_describe = "v0.0-9554-g862155839"
data_git_msg = """\
commit 862155839d7ff9b26c5515b49717a34554997b73
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Jan 20 17:34:28 2022 -0800

    [aes] update AES version in synthesis configs
    
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
