import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5773"
version_tuple = (0, 0, 5773)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5773")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5678"
data_version_tuple = (0, 0, 5678)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5678")
except ImportError:
    pass
data_git_hash = "72b1230e9e0063625d7c8e3da60fb957627cdfe5"
data_git_describe = "v0.0-5678-g72b1230e9"
data_git_msg = """\
commit 72b1230e9e0063625d7c8e3da60fb957627cdfe5
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Apr 7 13:31:22 2021 -0700

    [csrng/rtl] prevent x's from entering prim_arbiter_ppc_acmd
    
    Changing the data bus mux that feeds the app cmd arbiter to send zeros instead of x's when the mop signal is active.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
