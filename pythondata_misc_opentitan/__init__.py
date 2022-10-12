import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14707"
version_tuple = (0, 0, 14707)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14707")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14565"
data_version_tuple = (0, 0, 14565)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14565")
except ImportError:
    pass
data_git_hash = "a1ae9ba979aa1b47f978d8f5cd9bca6501f8e891"
data_git_describe = "v0.0-14565-ga1ae9ba979"
data_git_msg = """\
commit a1ae9ba979aa1b47f978d8f5cd9bca6501f8e891
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Oct 11 23:40:48 2022 +0000

    [flash_ctrl,dv] Add clocking block and input output slack
    
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
