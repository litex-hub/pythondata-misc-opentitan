import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14293"
version_tuple = (0, 0, 14293)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14293")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14151"
data_version_tuple = (0, 0, 14151)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14151")
except ImportError:
    pass
data_git_hash = "3d8aaefa4dd79b284cd65907b5728f5384399119"
data_git_describe = "v0.0-14151-g3d8aaefa4d"
data_git_msg = """\
commit 3d8aaefa4dd79b284cd65907b5728f5384399119
Author: Weicai Yang <weicai@google.com>
Date:   Sun Sep 18 23:05:00 2022 -0700

    [spi_device/dv] Fix xcelium errors
    
    2 places that kill the thread when csb is dropped, which caused errors in xcelium
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
