import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13270"
version_tuple = (0, 0, 13270)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13270")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13128"
data_version_tuple = (0, 0, 13128)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13128")
except ImportError:
    pass
data_git_hash = "6f14afac37d1b9d1fb0d66ff4cbffae8e1bda895"
data_git_describe = "v0.0-13128-g6f14afac37"
data_git_msg = """\
commit 6f14afac37d1b9d1fb0d66ff4cbffae8e1bda895
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Jul 25 17:45:56 2022 -0700

    [dv, waves] Improve wave dumping
    
    A minor non-functional change to waves.tcl improves the way
    wavedumpScope method is used to dump specific hierarchies
    rather than dump the tb top by default.
    
    The code is rearranged a little, and several comments are added
    to make the usage clearer. the `fid` argument of `wavedumpScope
    proc is removed in favor of using the value internally by
    referencing a global variable instead of passing it as an arg.
    
    Wavedumping has been tested with vcs:fsdb,vpd,vcd and
    xcelium:shm,fsdb and everything seeems to be working ok.
    
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
