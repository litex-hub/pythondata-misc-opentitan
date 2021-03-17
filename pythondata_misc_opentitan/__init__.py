import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5430"
version_tuple = (0, 0, 5430)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5430")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5335"
data_version_tuple = (0, 0, 5335)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5335")
except ImportError:
    pass
data_git_hash = "4853e5792c61b6c20b8a4839b157f27e5f140211"
data_git_describe = "v0.0-5335-g4853e5792"
data_git_msg = """\
commit 4853e5792c61b6c20b8a4839b157f27e5f140211
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 16 17:36:45 2021 -0700

    [fpv] compile issue fix
    
    This PR fixes two compile issue:
    1. SPI_DEVICE the fpv.tcl script has a signal name mismatch
    2. AES has an issue where input is recogized as an array
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
