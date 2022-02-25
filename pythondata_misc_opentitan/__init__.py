import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10540"
version_tuple = (0, 0, 10540)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10540")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10414"
data_version_tuple = (0, 0, 10414)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10414")
except ImportError:
    pass
data_git_hash = "f2ee5f1e5f864514ad60ee85d5bee07e45c69417"
data_git_describe = "v0.0-10414-gf2ee5f1e5"
data_git_msg = """\
commit f2ee5f1e5f864514ad60ee85d5bee07e45c69417
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 24 23:26:47 2022 +0000

    [otbn,rtl] Remove (unused) part of decoder supporting AUIPC
    
    We don't actually have that instruction! Spotted by a coverage hole.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
