import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12603"
version_tuple = (0, 0, 12603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12461"
data_version_tuple = (0, 0, 12461)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12461")
except ImportError:
    pass
data_git_hash = "64239cc7af46338e99d51362f1e42718b001bf4a"
data_git_describe = "v0.0-12461-g64239cc7a"
data_git_msg = """\
commit 64239cc7af46338e99d51362f1e42718b001bf4a
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jun 8 10:38:02 2022 -0400

    [sw/silicon_creator] Update CREATOR_SW_CFG_ROM_EXEC_EN for RMA and DEV OTP images
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
