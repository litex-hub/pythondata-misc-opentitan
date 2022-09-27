import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14440"
version_tuple = (0, 0, 14440)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14440")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14298"
data_version_tuple = (0, 0, 14298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14298")
except ImportError:
    pass
data_git_hash = "5b95d019b95423b14e590a285475abf4d99c50f6"
data_git_describe = "v0.0-14298-g5b95d019b9"
data_git_msg = """\
commit 5b95d019b95423b14e590a285475abf4d99c50f6
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Sep 19 13:35:35 2022 -0700

    [dv/rstmgr] Fix dv for recent changes in reset
    
    The recent RTL changes required big changes in the dv environment.
    This change disables non-aon clocks upon reset, and improves the
    flow of reset stimulus.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
