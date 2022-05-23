import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12271"
version_tuple = (0, 0, 12271)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12271")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12143"
data_version_tuple = (0, 0, 12143)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12143")
except ImportError:
    pass
data_git_hash = "46e134fa9faf6652c6ee4a05fd5cb138d32508ae"
data_git_describe = "v0.0-12143-g46e134fa9"
data_git_msg = """\
commit 46e134fa9faf6652c6ee4a05fd5cb138d32508ae
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri May 20 17:26:23 2022 +0100

    [otbn,doc] Reword documentation of the RND ISPR
    
    This is mostly just a rejig to make it easier to understand. But it
    also documents the new cache-clearing behaviour implemented in
    8e97525.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
