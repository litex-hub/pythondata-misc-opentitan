import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13096"
version_tuple = (0, 0, 13096)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13096")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12954"
data_version_tuple = (0, 0, 12954)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12954")
except ImportError:
    pass
data_git_hash = "ac5c373fcaf419c638dc9b6503084b630ec5470a"
data_git_describe = "v0.0-12954-gac5c373fca"
data_git_msg = """\
commit ac5c373fcaf419c638dc9b6503084b630ec5470a
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jul 14 14:05:05 2022 -0700

    [spi_dev/dv] Update scb to check passthrough items
    
    1. compare upstream items with downstream items
    2. some minor fixes
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
