import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14399"
version_tuple = (0, 0, 14399)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14399")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14257"
data_version_tuple = (0, 0, 14257)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14257")
except ImportError:
    pass
data_git_hash = "3603770f9085310a39aac00455d4fecde6bf7826"
data_git_describe = "v0.0-14257-g3603770f90"
data_git_msg = """\
commit 3603770f9085310a39aac00455d4fecde6bf7826
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Sep 13 09:48:26 2022 +0100

    [otbn,dv] Update testplan for countermeasures
    
    With PR #14322 *.SCA and *.SEC_WIPE countermeasures can be considered
    verified with the assertions.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
