import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11140"
version_tuple = (0, 0, 11140)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11140")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11014"
data_version_tuple = (0, 0, 11014)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11014")
except ImportError:
    pass
data_git_hash = "84c0e488ff31962b3226d4721fa7e7b17fd4eba3"
data_git_describe = "v0.0-11014-g84c0e488f"
data_git_msg = """\
commit 84c0e488ff31962b3226d4721fa7e7b17fd4eba3
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Mar 24 16:17:52 2022 -0700

    [bazel,dvsim] Add build rules for dvsim.py
    
    This adds bazel rules for dvsim.py so that it can be used by
    the opentitan_functest macro as a test runner (and dependency).
    
    This partially addresses #11684.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
