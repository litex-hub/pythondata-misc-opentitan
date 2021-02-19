import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5054"
version_tuple = (0, 0, 5054)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5054")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4963"
data_version_tuple = (0, 0, 4963)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4963")
except ImportError:
    pass
data_git_hash = "2aff11b701632ec81fefedae21fc8d9c30c87ec5"
data_git_describe = "v0.0-4963-g2aff11b70"
data_git_msg = """\
commit 2aff11b701632ec81fefedae21fc8d9c30c87ec5
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Feb 16 17:11:37 2021 +0000

    [ci] Move "slow lint" commands into script
    
    This should work the same as before, but is easier to run locally.
    Also, the job is no longer marked as "always()", which means it won't
    run if installing the package dependencies fails (which caused rather
    confusing error messages).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
