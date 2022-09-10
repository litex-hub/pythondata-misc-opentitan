import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14115"
version_tuple = (0, 0, 14115)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14115")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13973"
data_version_tuple = (0, 0, 13973)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13973")
except ImportError:
    pass
data_git_hash = "c4d76f7d41a4072a5d0a8e1da5634af66209a4b3"
data_git_describe = "v0.0-13973-gc4d76f7d41"
data_git_msg = """\
commit c4d76f7d41a4072a5d0a8e1da5634af66209a4b3
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Sep 6 17:21:29 2022 +0000

    [chip,dv,i2c] add loopback mode to i2c agent
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
