import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10900"
version_tuple = (0, 0, 10900)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10900")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10774"
data_version_tuple = (0, 0, 10774)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10774")
except ImportError:
    pass
data_git_hash = "009aa4b83fc2a229fa97b36f433c5e63d36d689e"
data_git_describe = "v0.0-10774-g009aa4b83"
data_git_msg = """\
commit 009aa4b83fc2a229fa97b36f433c5e63d36d689e
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Mar 15 09:27:09 2022 -0700

    [dv/rstmgr] Declare V2
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
