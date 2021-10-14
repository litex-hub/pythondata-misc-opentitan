import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8259"
version_tuple = (0, 0, 8259)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8259")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8147"
data_version_tuple = (0, 0, 8147)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8147")
except ImportError:
    pass
data_git_hash = "22af1e8d98b1a1753af0e34ef37ed333fc082c4a"
data_git_describe = "v0.0-8147-g22af1e8d9"
data_git_msg = """\
commit 22af1e8d98b1a1753af0e34ef37ed333fc082c4a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Oct 13 15:46:39 2021 +0100

    [otbn,dv] Sample RTL signals on first cycle of instruction
    
    We sample various internal RTL signals in order to do coverage
    collection. These are supposed to be "the value of the state just
    before the instruction ran". Most of the time, this is the same as
    "the value of the state just before the last cycle of running the
    instruction", but that's not quite always true.
    
    In particular, consider the following instruction:
    
      BN.LID x1, 0(x0)
    
    This reads from the call stack (x1) in order to get a destination
    address. With the current RTL implementation, the call stack pop
    happens on the first cycle which means that the previous code was
    sampling too late and saw an empty call stack. We wouldn't have
    noticed, except that the checks on "lockl_x1_uflow" in otbn_env_cov
    were failing (because we thought we should have seen a call stack
    underflow and the RTL disagreed).
    
    Fixes #8587.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
