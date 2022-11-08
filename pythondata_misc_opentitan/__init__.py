import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15326"
version_tuple = (0, 0, 15326)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15326")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15184"
data_version_tuple = (0, 0, 15184)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15184")
except ImportError:
    pass
data_git_hash = "32d4a1eefdbc2d6c440385e8153a48f6227ad6a2"
data_git_describe = "v0.0-15184-g32d4a1eefd"
data_git_msg = """\
commit 32d4a1eefdbc2d6c440385e8153a48f6227ad6a2
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 7 16:45:17 2022 -0800

    [keymgr/dv] Fix 2 regression failures
    
    1. Fixed scb for direct_to_disable test
    2. Disabled EDN SVA for CSR tests
    
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
