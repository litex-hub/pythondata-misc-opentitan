import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10625"
version_tuple = (0, 0, 10625)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10625")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10499"
data_version_tuple = (0, 0, 10499)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10499")
except ImportError:
    pass
data_git_hash = "fb5194f6f7838e92667f2f01e9f87bdaea87aa6f"
data_git_describe = "v0.0-10499-gfb5194f6f"
data_git_msg = """\
commit fb5194f6f7838e92667f2f01e9f87bdaea87aa6f
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Feb 25 10:20:59 2022 -0800

    [dv/rstmgr] Add missing covergroups
    
    Also fix related dv doc mistakes.
    
    Fixes #10687
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
