import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10771"
version_tuple = (0, 0, 10771)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10771")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10645"
data_version_tuple = (0, 0, 10645)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10645")
except ImportError:
    pass
data_git_hash = "7c4f8b3fde4bb625ac3330ff52d3f66507190fe5"
data_git_describe = "v0.0-10645-g7c4f8b3fd"
data_git_msg = """\
commit 7c4f8b3fde4bb625ac3330ff52d3f66507190fe5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 7 12:41:52 2022 +0000

    [dv,lc_ctrl] Make two static functions automatic
    
    These functions are marked static but I don't think there's any
    particular reason to do so. They each have local
    variables (err_inj_idx) and Xcelium issues a warning because these
    aren't also explicitly marked as static. A good warning, because it's
    a "foot gun" just waiting to catch you out!
    
    Let's just make the functions automatic and not worry about it.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
