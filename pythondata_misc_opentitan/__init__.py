import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8749"
version_tuple = (0, 0, 8749)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8749")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8637"
data_version_tuple = (0, 0, 8637)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8637")
except ImportError:
    pass
data_git_hash = "c2ae2ea26d14b7df8f12edc6c1aa97f1a0797e80"
data_git_describe = "v0.0-8637-gc2ae2ea26"
data_git_msg = """\
commit c2ae2ea26d14b7df8f12edc6c1aa97f1a0797e80
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 15 17:45:15 2021 -0800

    [sram/dv] update scb and seq for exec test and tl_err test
    
    1. simplify seq to randomize mubi and lc_tx variables
    2. update scb to fix tl_err test
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
