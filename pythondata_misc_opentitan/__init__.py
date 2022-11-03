import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15167"
version_tuple = (0, 0, 15167)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15167")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15025"
data_version_tuple = (0, 0, 15025)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15025")
except ImportError:
    pass
data_git_hash = "cbba276294efa163b5c5be029a9487c9908d9dd2"
data_git_describe = "v0.0-15025-gcbba276294"
data_git_msg = """\
commit cbba276294efa163b5c5be029a9487c9908d9dd2
Author: James Wainwright <james.wainwright@lowrisc.org>
Date:   Thu Oct 20 16:39:18 2022 +0100

    [docs] Add styleguide example for documented struct
    
    Clarifies that block comments should be used for structs and struct members as
    well as functions.
    
    Signed-off-by: James Wainwright <james.wainwright@lowrisc.org>

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
