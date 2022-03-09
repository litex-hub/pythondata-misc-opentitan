import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10800"
version_tuple = (0, 0, 10800)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10800")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10674"
data_version_tuple = (0, 0, 10674)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10674")
except ImportError:
    pass
data_git_hash = "b067c3927d260cc1efac0f8b0564610d510697bb"
data_git_describe = "v0.0-10674-gb067c3927"
data_git_msg = """\
commit b067c3927d260cc1efac0f8b0564610d510697bb
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Mar 3 14:39:23 2022 -0800

    [fpv/pinmux] V2 checklist
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
