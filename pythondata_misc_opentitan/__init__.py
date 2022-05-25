import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12306"
version_tuple = (0, 0, 12306)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12306")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12175"
data_version_tuple = (0, 0, 12175)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12175")
except ImportError:
    pass
data_git_hash = "10e1dc67b3d946d988a7f5bc3e960ca447dff2c0"
data_git_describe = "v0.0-12175-g10e1dc67b"
data_git_msg = """\
commit 10e1dc67b3d946d988a7f5bc3e960ca447dff2c0
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Tue May 24 17:17:50 2022 -0700

    [sw/silicon_creator] Add manuf state OTP fields
    
    Add manufacturing state OTP values for creator and owner manufacturing
    stages. The Silicon Creator and Silicon Owner can constraint manifest
    signatures to devices with a configured manuf state OTP value. Creator
    and Owner stage values are available to accomodate for manufacturing
    flows that perform Silicon Owner SKU configuration at a different time
    from personalization.
    
    This resolves issue #7948
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post131"
tool_version_tuple = (0, 0, 131)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post131")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
