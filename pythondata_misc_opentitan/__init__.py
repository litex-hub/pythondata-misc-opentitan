import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9290"
version_tuple = (0, 0, 9290)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9290")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9173"
data_version_tuple = (0, 0, 9173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9173")
except ImportError:
    pass
data_git_hash = "854388d4644276f097acdacb1f4ed356b2d04ce2"
data_git_describe = "v0.0-9173-g854388d46"
data_git_msg = """\
commit 854388d4644276f097acdacb1f4ed356b2d04ce2
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Dec 23 13:58:25 2021 -0800

    [fpv/pinmux] Update pinmux existing assertions
    
    This PR updates the currect assertions to consider two more cases: sleep
    and jtag.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
