import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8774"
version_tuple = (0, 0, 8774)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8774")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8662"
data_version_tuple = (0, 0, 8662)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8662")
except ImportError:
    pass
data_git_hash = "06d51db034c5a1792300bba57289c99701a73458"
data_git_describe = "v0.0-8662-g06d51db03"
data_git_msg = """\
commit 06d51db034c5a1792300bba57289c99701a73458
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Nov 18 10:30:31 2021 -0500

    [sw/silicon_creator] Migrate boot_data_functest to silicon_creator flash_ctrl driver
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
