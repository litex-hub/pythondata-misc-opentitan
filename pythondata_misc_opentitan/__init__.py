import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9981"
version_tuple = (0, 0, 9981)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9981")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9857"
data_version_tuple = (0, 0, 9857)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9857")
except ImportError:
    pass
data_git_hash = "c0b2ef5041e8d34f264b2ddaccc8d5cfdb97b413"
data_git_describe = "v0.0-9857-gc0b2ef504"
data_git_msg = """\
commit c0b2ef5041e8d34f264b2ddaccc8d5cfdb97b413
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Feb 1 15:21:03 2022 -0800

    [fpv] Fix gui mode switch
    
    This PR fixes the switch to use GUI mode:
    When `-batch` it will be batch mode;
    When `` it will be gui mode.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
