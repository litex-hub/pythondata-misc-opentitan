import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9770"
version_tuple = (0, 0, 9770)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9770")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9648"
data_version_tuple = (0, 0, 9648)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9648")
except ImportError:
    pass
data_git_hash = "5730f0d9ff12ce152b6333aa8cd738c32c419e40"
data_git_describe = "v0.0-9648-g5730f0d9f"
data_git_msg = """\
commit 5730f0d9ff12ce152b6333aa8cd738c32c419e40
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Jan 24 14:57:51 2022 +0000

    [otbn,dv] Commit GPR changes when stalled
    
    This only really makes a difference for BN.LID instructions like this:
    
        bn.lid x15++, 1184(x22)
    
    Here, the RTL increments x15 on the first cycle. If the load triggered
    an error because the DMEM integrity bits were malformed, all
    side-effects of the instruction will have been discarded except for
    the write to x15.
    
    Until this change, the ISS committed the GPR change on the second
    cycle. Of course, this meant that the aborting instruction would not
    commit the GPR change at all, resulting in a mismatch between RTL and
    ISS for the final state.
    
    Note that this difference isn't actually observable in the design:
    there's no bus access to register values and we will wipe the register
    file between operations. But it *did* cause test failures because we
    have a comparison of post-run dumps. Those should be fixed now.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
