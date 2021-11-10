import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8659"
version_tuple = (0, 0, 8659)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8659")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8547"
data_version_tuple = (0, 0, 8547)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8547")
except ImportError:
    pass
data_git_hash = "19b727d437dd893125cf08f68a79f819b2b664a7"
data_git_describe = "v0.0-8547-g19b727d43"
data_git_msg = """\
commit 19b727d437dd893125cf08f68a79f819b2b664a7
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Tue Nov 9 11:48:06 2021 +0000

    [hw, hjson] SRAM Controller use `multibits.h` in register desc
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
