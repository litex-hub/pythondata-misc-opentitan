import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9307"
version_tuple = (0, 0, 9307)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9307")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9190"
data_version_tuple = (0, 0, 9190)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9190")
except ImportError:
    pass
data_git_hash = "76bb780cf56fc9d2375f8f9d1cb04f337516a0f3"
data_git_describe = "v0.0-9190-g76bb780cf"
data_git_msg = """\
commit 76bb780cf56fc9d2375f8f9d1cb04f337516a0f3
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Dec 29 14:11:28 2021 -0800

    [fpv/pinmux] Tapstrap assertion
    
    This PR adds assertions on pinmux tapstrap selection.
    
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
