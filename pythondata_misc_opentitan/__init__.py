import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10411"
version_tuple = (0, 0, 10411)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10411")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10285"
data_version_tuple = (0, 0, 10285)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10285")
except ImportError:
    pass
data_git_hash = "47b50cbcbb9ae8a331310e4ea4befca0c2c130a4"
data_git_describe = "v0.0-10285-g47b50cbcb"
data_git_msg = """\
commit 47b50cbcbb9ae8a331310e4ea4befca0c2c130a4
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Feb 17 12:20:08 2022 -0800

    [kmac] Regenerate TOP Earlgrey
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
