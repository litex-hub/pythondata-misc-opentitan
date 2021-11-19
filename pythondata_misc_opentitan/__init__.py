import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8784"
version_tuple = (0, 0, 8784)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8784")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8672"
data_version_tuple = (0, 0, 8672)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8672")
except ImportError:
    pass
data_git_hash = "74d7e11098b51183c948a263fa8db6f7c489fe4c"
data_git_describe = "v0.0-8672-g74d7e1109"
data_git_msg = """\
commit 74d7e11098b51183c948a263fa8db6f7c489fe4c
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Nov 16 18:25:49 2021 +0000

    [sw] Clean up the mtvec loading code
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
