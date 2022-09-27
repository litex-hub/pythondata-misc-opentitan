import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14464"
version_tuple = (0, 0, 14464)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14464")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14322"
data_version_tuple = (0, 0, 14322)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14322")
except ImportError:
    pass
data_git_hash = "97d123b67eccfea340e56717afdbc1dfe5d8a510"
data_git_describe = "v0.0-14322-g97d123b67e"
data_git_msg = """\
commit 97d123b67eccfea340e56717afdbc1dfe5d8a510
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Sep 26 14:34:58 2022 -0700

    address review comments
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
