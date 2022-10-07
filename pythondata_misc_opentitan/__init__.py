import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14624"
version_tuple = (0, 0, 14624)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14624")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14482"
data_version_tuple = (0, 0, 14482)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14482")
except ImportError:
    pass
data_git_hash = "a10c750572c18933a8fd769b7411dbbd9d88c64f"
data_git_describe = "v0.0-14482-ga10c750572"
data_git_msg = """\
commit a10c750572c18933a8fd769b7411dbbd9d88c64f
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Sep 26 15:46:24 2022 +0000

    [pwrmgr,dv] Sign off V2S
    
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
