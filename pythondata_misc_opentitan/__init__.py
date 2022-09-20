import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14311"
version_tuple = (0, 0, 14311)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14311")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14169"
data_version_tuple = (0, 0, 14169)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14169")
except ImportError:
    pass
data_git_hash = "902ca28e32018f7fb4f3db9e71fdf395ced7ed09"
data_git_describe = "v0.0-14169-g902ca28e32"
data_git_msg = """\
commit 902ca28e32018f7fb4f3db9e71fdf395ced7ed09
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Sep 19 18:04:51 2022 -0700

    [chip dv] Fix JTAG interface enablement
    
    THe previous code relied on the test bench setting the TAP
    strap pins to enable the JTAG interface, rather than adding
    a dedicated `enable_jtag` mux signal.
    
    The existing code looked at the `tap_straps_if.pins`, which
    is just a wire which will reflect the value of the pins
    IOC5,8 which may have been wiggled for a different test with
    a different interface, and that would inadvertantly end up
    enabling JTAG, causing contention.
    
    This commit makes it look at both, the `pins_o` and `pins_oe`
    values, so that the actual intent of setting the TAP straps
    is what causes the JTAG to be enabled.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
