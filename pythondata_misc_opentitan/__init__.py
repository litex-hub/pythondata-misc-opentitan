import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5541"
version_tuple = (0, 0, 5541)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5541")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5446"
data_version_tuple = (0, 0, 5446)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5446")
except ImportError:
    pass
data_git_hash = "5c6da15f1b279a95d189974795edcb510c0e2323"
data_git_describe = "v0.0-5446-g5c6da15f1"
data_git_msg = """\
commit 5c6da15f1b279a95d189974795edcb510c0e2323
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 23 16:44:40 2021 -0700

    [fpv/rstmgr] FPV compile error
    
    This PR fixes a compile error in FPV. I will contact the AE and see if
    they can fix it. Right now the prim_lc_sync syntax works for simulation
    but not FPV.
    
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
