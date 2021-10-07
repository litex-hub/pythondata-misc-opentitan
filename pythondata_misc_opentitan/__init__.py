import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8165"
version_tuple = (0, 0, 8165)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8165")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8053"
data_version_tuple = (0, 0, 8053)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8053")
except ImportError:
    pass
data_git_hash = "bb7c48f3cd8c857d0dead658232f738236f66364"
data_git_describe = "v0.0-8053-gbb7c48f3c"
data_git_msg = """\
commit bb7c48f3cd8c857d0dead658232f738236f66364
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Oct 6 11:32:14 2021 +0100

    [otbn,dv] Proper Connection of EDN_IF to OTBN
    
    In this commit an EDN interface is connected at the block level
    testbench of OTBN. Also incoming RND data packages are now arranged
    in a way that the first package would be at the bottom 32b of RND
    register.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
