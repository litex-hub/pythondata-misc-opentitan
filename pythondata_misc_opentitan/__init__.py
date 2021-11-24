import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8857"
version_tuple = (0, 0, 8857)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8857")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8745"
data_version_tuple = (0, 0, 8745)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8745")
except ImportError:
    pass
data_git_hash = "c6030a4ad3230fbe093e5ce8012e2b25ae52343f"
data_git_describe = "v0.0-8745-gc6030a4ad"
data_git_msg = """\
commit c6030a4ad3230fbe093e5ce8012e2b25ae52343f
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Nov 23 16:52:18 2021 +0000

    [sw/silicon_creator] Separate mask ROM specific RSA subroutines.
    
    Create a separate interface for RSA-3072 that has only the subroutines
    mask ROM needs, and write a separate C wrapper for that interface.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
