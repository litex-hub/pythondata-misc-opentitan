import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5699"
version_tuple = (0, 0, 5699)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5699")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5604"
data_version_tuple = (0, 0, 5604)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5604")
except ImportError:
    pass
data_git_hash = "f309ea551de2c7dea8024a9002f7086591177952"
data_git_describe = "v0.0-5604-gf309ea551"
data_git_msg = """\
commit f309ea551de2c7dea8024a9002f7086591177952
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Apr 1 18:16:57 2021 -0700

    [fpv] revert back the FPV compile error
    
    This PR revert back the previous workaround to avoid the compile error.
    Now the JasperGold is fixed to support this `prim_lc_sync` syntax.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
