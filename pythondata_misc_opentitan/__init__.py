import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10266"
version_tuple = (0, 0, 10266)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10266")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10142"
data_version_tuple = (0, 0, 10142)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10142")
except ImportError:
    pass
data_git_hash = "e98fba4dcf4aa84327bda9865791890e64ac8c41"
data_git_describe = "v0.0-10142-ge98fba4dc"
data_git_msg = """\
commit e98fba4dcf4aa84327bda9865791890e64ac8c41
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 11 12:14:17 2022 -0800

    [dv/kmac] Add a kmac_if interface
    
    Add a kmac_if interface to:
    1). Drive lc_escalation input.
    2). Replace the extra pin `idle` and add it to kmac interface.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
