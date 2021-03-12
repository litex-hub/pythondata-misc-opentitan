import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5368"
version_tuple = (0, 0, 5368)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5368")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5273"
data_version_tuple = (0, 0, 5273)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5273")
except ImportError:
    pass
data_git_hash = "0cdc34477a53e9958d4cd1d22604a64a1f383b5a"
data_git_describe = "v0.0-5273-g0cdc34477"
data_git_msg = """\
commit 0cdc34477a53e9958d4cd1d22604a64a1f383b5a
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Mar 11 03:40:15 2021 -0800

    [entropy_src/rtl] remove duplicate parameter
    
    The EsFifoDepth parameter will now only be set in the top file.
    This parameter is set to the same default value in all cases.
    Increasing the depth requires a width increase to the debug register.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
