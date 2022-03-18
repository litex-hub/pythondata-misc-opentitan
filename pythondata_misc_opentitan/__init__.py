import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10985"
version_tuple = (0, 0, 10985)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10985")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10859"
data_version_tuple = (0, 0, 10859)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10859")
except ImportError:
    pass
data_git_hash = "67e117d85a9db1e5a0ae94f79762ceb1aaf26570"
data_git_describe = "v0.0-10859-g67e117d85"
data_git_msg = """\
commit 67e117d85a9db1e5a0ae94f79762ceb1aaf26570
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Mar 18 09:17:17 2022 -0700

    [doc/clkmgr] Fix trivial typo
    
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
