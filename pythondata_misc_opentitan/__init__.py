import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9324"
version_tuple = (0, 0, 9324)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9324")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9207"
data_version_tuple = (0, 0, 9207)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9207")
except ImportError:
    pass
data_git_hash = "7d2b7999be34022174ce5f112eb2bb573164c389"
data_git_describe = "v0.0-9207-g7d2b7999b"
data_git_msg = """\
commit 7d2b7999be34022174ce5f112eb2bb573164c389
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Tue Dec 28 06:45:22 2021 -0800

    [csrng/rtl] fsm default value incorrect
    
    While doing state machine error testing, the default value for the drbg_updob fsm was found to be incorrect.
    It needs to be the error state.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
