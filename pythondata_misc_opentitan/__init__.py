import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8204"
version_tuple = (0, 0, 8204)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8204")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8092"
data_version_tuple = (0, 0, 8092)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8092")
except ImportError:
    pass
data_git_hash = "16049df3f36306b8d02f640f7e96223223202bd8"
data_git_describe = "v0.0-8092-g16049df3f"
data_git_msg = """\
commit 16049df3f36306b8d02f640f7e96223223202bd8
Author: Michael Schaffner <msf@google.com>
Date:   Mon Oct 4 16:29:55 2021 -0700

    [alert_handler/doc] Update documentation with LPG feature
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
