import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10092"
version_tuple = (0, 0, 10092)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10092")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9968"
data_version_tuple = (0, 0, 9968)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9968")
except ImportError:
    pass
data_git_hash = "e2400ae71311eb3d91b5760b13c26b9c1abbe43c"
data_git_describe = "v0.0-9968-ge2400ae71"
data_git_msg = """\
commit e2400ae71311eb3d91b5760b13c26b9c1abbe43c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 16 11:31:03 2021 -0800

    [fpv/prim_count] Inject fault to ensure counter errors are hit
    
    This PR injects errors by inserting stopat to make sure the counters hit
    proper error assertions.
    
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
