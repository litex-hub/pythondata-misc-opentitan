import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13165"
version_tuple = (0, 0, 13165)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13165")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13023"
data_version_tuple = (0, 0, 13023)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13023")
except ImportError:
    pass
data_git_hash = "50f9473215091f932d6936c3ebc35a5df14b4488"
data_git_describe = "v0.0-13023-g50f9473215"
data_git_msg = """\
commit 50f9473215091f932d6936c3ebc35a5df14b4488
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jul 18 17:02:02 2022 -0700

    [dv/kmac] Fix unmasked_error code failure
    
    This PR fixes the regression failure at error sequence.
    The issue is due to newly support field `en_unsupported_modestrength`.
    Current randomization only allow this field to be 1. There is still a
    testbench(scb) error when value is set to 0.
    I will work on fixing this issue asap.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
