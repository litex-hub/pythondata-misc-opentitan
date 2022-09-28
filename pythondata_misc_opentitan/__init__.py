import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14486"
version_tuple = (0, 0, 14486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14344"
data_version_tuple = (0, 0, 14344)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14344")
except ImportError:
    pass
data_git_hash = "7550a3512290c3c4df978fcc70112b787c963076"
data_git_describe = "v0.0-14344-g7550a35122"
data_git_msg = """\
commit 7550a3512290c3c4df978fcc70112b787c963076
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Sep 27 17:51:44 2022 -0700

    [bazel] remove unused build targets
    
    It looks like these build targets are unused / unnecessary as they are
    file groups that export a single target that could each be used
    directly.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
