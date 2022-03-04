import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10709"
version_tuple = (0, 0, 10709)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10709")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10583"
data_version_tuple = (0, 0, 10583)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10583")
except ImportError:
    pass
data_git_hash = "41742aa9b19b44e0fe81fc14fec2be0649c8a45d"
data_git_describe = "v0.0-10583-g41742aa9b"
data_git_msg = """\
commit 41742aa9b19b44e0fe81fc14fec2be0649c8a45d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Mar 3 12:32:12 2022 -0800

    [fpv/pinmux] Add an missing assertion from testplan
    
    Add a missing assertion `MioJtagAttrO_A`.
    
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
