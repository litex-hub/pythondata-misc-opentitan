import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8978"
version_tuple = (0, 0, 8978)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8978")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8866"
data_version_tuple = (0, 0, 8866)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8866")
except ImportError:
    pass
data_git_hash = "76e0cfa48f9a7e63093a949e19c20ed4baca805f"
data_git_describe = "v0.0-8866-g76e0cfa48"
data_git_msg = """\
commit 76e0cfa48f9a7e63093a949e19c20ed4baca805f
Author: Michael Schaffner <msf@google.com>
Date:   Thu Dec 2 15:28:25 2021 -0800

    [syn] Fix SDC constraint
    
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
