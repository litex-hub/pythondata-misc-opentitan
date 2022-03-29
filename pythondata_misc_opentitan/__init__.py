import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11182"
version_tuple = (0, 0, 11182)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11182")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11056"
data_version_tuple = (0, 0, 11056)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11056")
except ImportError:
    pass
data_git_hash = "d87e6127905ed7898234ccebe0e3b8d1ef20e138"
data_git_describe = "v0.0-11056-gd87e61279"
data_git_msg = """\
commit d87e6127905ed7898234ccebe0e3b8d1ef20e138
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Mar 25 08:57:54 2022 -0700

    [bazel] Automate download of `bazelisk`
    
    1. Create downloader script.
    2. Git ignore //.bin since we dont want to commit binaries to the codebase.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
