import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8391"
version_tuple = (0, 0, 8391)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8391")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8279"
data_version_tuple = (0, 0, 8279)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8279")
except ImportError:
    pass
data_git_hash = "0d9c43a552498ee2bbfbbe80e3f767066e572223"
data_git_describe = "v0.0-8279-g0d9c43a55"
data_git_msg = """\
commit 0d9c43a552498ee2bbfbbe80e3f767066e572223
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 20 21:13:29 2021 +0000

    [dif/sysrst_ctrl] Auto-generate portion of DIFs.
    
    Currently, the DIF library for the System Reset Control IP is
    unimplemented. This begins the implementation of this DIF library by
    first checking in the auto-generated DIFs (init and IRQ DIFs).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
