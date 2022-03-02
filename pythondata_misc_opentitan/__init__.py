import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10665"
version_tuple = (0, 0, 10665)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10665")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10539"
data_version_tuple = (0, 0, 10539)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10539")
except ImportError:
    pass
data_git_hash = "8eb2bc0879d85d0cd25aa3f6bbfb85f0bef69fb9"
data_git_describe = "v0.0-10539-g8eb2bc087"
data_git_msg = """\
commit 8eb2bc0879d85d0cd25aa3f6bbfb85f0bef69fb9
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Mar 1 14:29:09 2022 -0800

    [full_chip,clkmgr] Bind clkmgr SVA in full chip
    
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
