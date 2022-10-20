import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14851"
version_tuple = (0, 0, 14851)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14851")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14709"
data_version_tuple = (0, 0, 14709)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14709")
except ImportError:
    pass
data_git_hash = "a28800f5bf6874b38c20ed723e0bfab1d36519d4"
data_git_describe = "v0.0-14709-ga28800f5bf"
data_git_msg = """\
commit a28800f5bf6874b38c20ed723e0bfab1d36519d4
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 17 16:50:54 2022 -0700

    [spi_device/dv] Add stress_all test
    
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
