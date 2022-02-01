import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9975"
version_tuple = (0, 0, 9975)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9975")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9851"
data_version_tuple = (0, 0, 9851)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9851")
except ImportError:
    pass
data_git_hash = "0409944012596a05d679a976fa2510a5c73ad781"
data_git_describe = "v0.0-9851-g040994401"
data_git_msg = """\
commit 0409944012596a05d679a976fa2510a5c73ad781
Author: Michael Schaffner <msf@google.com>
Date:   Tue Feb 1 03:35:44 2022 +0000

    [fpga] Make divided clock constraint more precise
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
