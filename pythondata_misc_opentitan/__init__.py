import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9555"
version_tuple = (0, 0, 9555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9433"
data_version_tuple = (0, 0, 9433)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9433")
except ImportError:
    pass
data_git_hash = "50dd5699865d116ee0a313cbda096adf44576bca"
data_git_describe = "v0.0-9433-g50dd56998"
data_git_msg = """\
commit 50dd5699865d116ee0a313cbda096adf44576bca
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri Jan 14 12:02:31 2022 +0000

    [rom_ctrl, dv] V1 signoff
    
    All actions items from V1 review have been finished and PRs have been
    merged.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
