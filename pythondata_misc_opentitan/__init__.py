import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8334"
version_tuple = (0, 0, 8334)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8334")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8222"
data_version_tuple = (0, 0, 8222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8222")
except ImportError:
    pass
data_git_hash = "3cf9984c1fd7129f082b7d686d2bc17a27f61ab7"
data_git_describe = "v0.0-8222-g3cf9984c1"
data_git_msg = """\
commit 3cf9984c1fd7129f082b7d686d2bc17a27f61ab7
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Oct 18 10:38:45 2021 +0100

    [otbn,dv] Pick up extreme offset addresses for bne and be commands.
    
    Following additions/ changes have been made in this commit:
    1. Added a new variable called mode to assign equal weightage to all
    possible address ranges.
    2. Edited the randomization logic to pick up offset address.
    
    Fixes #8078
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
