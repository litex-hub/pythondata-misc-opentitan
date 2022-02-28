import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10583"
version_tuple = (0, 0, 10583)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10583")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10457"
data_version_tuple = (0, 0, 10457)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10457")
except ImportError:
    pass
data_git_hash = "0540f242cd078472e9a57042f19800973b4a9148"
data_git_describe = "v0.0-10457-g0540f242c"
data_git_msg = """\
commit 0540f242cd078472e9a57042f19800973b4a9148
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Fri Feb 18 03:49:59 2022 -0800

    [aes/dv] updated deinit to include trying to trigger start after clear
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
