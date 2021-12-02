import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8969"
version_tuple = (0, 0, 8969)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8969")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8857"
data_version_tuple = (0, 0, 8857)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8857")
except ImportError:
    pass
data_git_hash = "39a1822e6ce3ecd9af443525e41ed258d9225264"
data_git_describe = "v0.0-8857-g39a1822e6"
data_git_msg = """\
commit 39a1822e6ce3ecd9af443525e41ed258d9225264
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Nov 23 22:33:18 2021 +0000

    [ottf,mask_rom] Migrate all mask ROM func tests to OTTF.
    
    This commit migrates all mask ROM func tests to the OTTF, from the old
    (soon to be deprecated) on-device test framework.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
