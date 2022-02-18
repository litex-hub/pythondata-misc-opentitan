import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10443"
version_tuple = (0, 0, 10443)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10443")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10317"
data_version_tuple = (0, 0, 10317)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10317")
except ImportError:
    pass
data_git_hash = "5ee89951047ce0f3efe6a3b663451c20305e6faf"
data_git_describe = "v0.0-10317-g5ee899510"
data_git_msg = """\
commit 5ee89951047ce0f3efe6a3b663451c20305e6faf
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Feb 18 14:10:44 2022 -0800

    [lint] Increase the unroll count
    
    This commit increases Ascentlint max unroll count from 1024 (default) to
    3200 (max Kmac state x2)
    
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
