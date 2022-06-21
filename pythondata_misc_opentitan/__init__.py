import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12777"
version_tuple = (0, 0, 12777)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12777")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12635"
data_version_tuple = (0, 0, 12635)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12635")
except ImportError:
    pass
data_git_hash = "11984ce01ecdac82d21573454ff2d3610e10d95d"
data_git_describe = "v0.0-12635-g11984ce01e"
data_git_msg = """\
commit 11984ce01ecdac82d21573454ff2d3610e10d95d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jun 10 11:59:47 2022 -0700

    [dv/chip] Fix same_csr_outstanding error
    
    This PR fixes a csr outstanding error from pwrmgr, looks like it is
    excluded from block level already. And looking at the description from
    the hjson file, I think we mean to put a write exclude instead of a
    read exclude.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
