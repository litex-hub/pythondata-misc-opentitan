import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8450"
version_tuple = (0, 0, 8450)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8450")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8338"
data_version_tuple = (0, 0, 8338)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8338")
except ImportError:
    pass
data_git_hash = "4100db3899c8a6b26bcf377f825b5725af8c8091"
data_git_describe = "v0.0-8338-g4100db389"
data_git_msg = """\
commit 4100db3899c8a6b26bcf377f825b5725af8c8091
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 21 16:45:02 2021 +0100

    [pwrmgr,lint] Fix some width mismatches in pwrmgr_pkg
    
    These are all of the form "wide0 = wide1 + narrow" where wide* are
    integers and narrow is an enum value that's just a couple of bits
    wide. Make the widening to int explicit to silence the Verilator
    warning.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
