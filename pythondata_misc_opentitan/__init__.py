import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5064"
version_tuple = (0, 0, 5064)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5064")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4973"
data_version_tuple = (0, 0, 4973)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4973")
except ImportError:
    pass
data_git_hash = "c7f52e91e14d76bc1049f5def17a6f4607d0c658"
data_git_describe = "v0.0-4973-gc7f52e91e"
data_git_msg = """\
commit c7f52e91e14d76bc1049f5def17a6f4607d0c658
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Feb 19 12:23:40 2021 +0000

    [topgen] Demote message about xbar connections from warning to info
    
    This is just how we wire up our chip at the moment, so a warning
    doesn't seem like the right thing to do!
    
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
