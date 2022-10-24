import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14919"
version_tuple = (0, 0, 14919)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14919")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14777"
data_version_tuple = (0, 0, 14777)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14777")
except ImportError:
    pass
data_git_hash = "d68e7cbb925fee1d1daa09dd1fc3e697774fb31b"
data_git_describe = "v0.0-14777-gd68e7cbb92"
data_git_msg = """\
commit d68e7cbb925fee1d1daa09dd1fc3e697774fb31b
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 24 13:15:12 2022 -0700

    [spi_device/dv] Fix a race condition
    
    `1ps` is already used to handle downstream item comparison.
    Increased to 2ps. This fixes many failures in flash related tests.
    
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
