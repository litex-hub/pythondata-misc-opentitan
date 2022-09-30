import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14522"
version_tuple = (0, 0, 14522)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14522")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14380"
data_version_tuple = (0, 0, 14380)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14380")
except ImportError:
    pass
data_git_hash = "841a2b6d62e911fa8d5572cecd7f4f436aa420d7"
data_git_describe = "v0.0-14380-g841a2b6d62"
data_git_msg = """\
commit 841a2b6d62e911fa8d5572cecd7f4f436aa420d7
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Sep 29 08:48:46 2022 -0400

    [test] Add remaining tests for rom_e2e_address_translation
    
    Fixes #14483
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
