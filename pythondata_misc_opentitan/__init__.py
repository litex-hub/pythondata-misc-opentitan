import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8249"
version_tuple = (0, 0, 8249)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8249")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8137"
data_version_tuple = (0, 0, 8137)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8137")
except ImportError:
    pass
data_git_hash = "febdee3ea9134ebfbaf12fe276cdf6e747129ee1"
data_git_describe = "v0.0-8137-gfebdee3ea"
data_git_msg = """\
commit febdee3ea9134ebfbaf12fe276cdf6e747129ee1
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Oct 5 17:45:09 2021 -0700

    [sw/clkmgr_testutils] Add clkmgr testutils
    
    Added these to make `aes_idle.c` test in PR #8451 a bit more
    streamlined. These utils will be needed in other idle tests.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
