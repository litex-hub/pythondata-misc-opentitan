import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8372"
version_tuple = (0, 0, 8372)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8372")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8260"
data_version_tuple = (0, 0, 8260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8260")
except ImportError:
    pass
data_git_hash = "8d876f10990d516ed83e3b058d089fd3e7176380"
data_git_describe = "v0.0-8260-g8d876f109"
data_git_msg = """\
commit 8d876f10990d516ed83e3b058d089fd3e7176380
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Oct 20 17:10:55 2021 +0100

    [otbn/util] Update RISC-V toolchain search to look in default location.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
