import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13234"
version_tuple = (0, 0, 13234)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13234")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13092"
data_version_tuple = (0, 0, 13092)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13092")
except ImportError:
    pass
data_git_hash = "76a7f60d94dfeae29b28063650ba224d4c4f9d9e"
data_git_describe = "v0.0-13092-g76a7f60d94"
data_git_msg = """\
commit 76a7f60d94dfeae29b28063650ba224d4c4f9d9e
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Tue Jul 19 09:38:24 2022 +0100

    [sca/kmac] Switch off entropy fast process
    
    Entropy fast process should not be used in scenarios which require
    side-channel security.
    This commit switches off entropy fast process in sha3_serial.c and
    updates documentation.
    
    Signed-off-by: Vladimir Rozic <vrozic@lowrisc.org>

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
