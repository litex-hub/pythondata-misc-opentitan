import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14861"
version_tuple = (0, 0, 14861)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14861")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14719"
data_version_tuple = (0, 0, 14719)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14719")
except ImportError:
    pass
data_git_hash = "f87a62c7caac83d83b32fcd699b3d9de20bf9aac"
data_git_describe = "v0.0-14719-gf87a62c7ca"
data_git_msg = """\
commit f87a62c7caac83d83b32fcd699b3d9de20bf9aac
Author: Dan McArdle <dmcardle@google.com>
Date:   Thu Oct 20 12:08:31 2022 -0400

    [sw] Invalidate icache in SRAM GDB test
    
    This commit also generalizes the test's success pattern so it does not
    care about the specific line number.
    
    Fixes #15595
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
