import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10083"
version_tuple = (0, 0, 10083)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10083")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9959"
data_version_tuple = (0, 0, 9959)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9959")
except ImportError:
    pass
data_git_hash = "d255d45f29a6af156a2df2a10e5e53aad777fde4"
data_git_describe = "v0.0-9959-gd255d45f2"
data_git_msg = """\
commit d255d45f29a6af156a2df2a10e5e53aad777fde4
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 4 00:12:57 2022 -0800

    [dv/otp_ctrl] Update UNR with blackbox
    
    This PR updates the UNR module with security modules being blackboxed.
    
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
