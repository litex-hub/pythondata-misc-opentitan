import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8336"
version_tuple = (0, 0, 8336)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8336")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8224"
data_version_tuple = (0, 0, 8224)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8224")
except ImportError:
    pass
data_git_hash = "c7585e793a8500811c2dfa2bfdab6975db75bb4f"
data_git_describe = "v0.0-8224-gc7585e793"
data_git_msg = """\
commit c7585e793a8500811c2dfa2bfdab6975db75bb4f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 19 12:12:19 2021 +0100

    [otbn,dv] Use clocking block to spot instruction execution
    
    This fixes a problem caused by us switching to spotting STATUS changes
    on the negedge of the clock (in commit bfe59f0a8).
    
    The problem is triggered when executing a final ECALL instruction or
    similar. The model immediately reports that STATUS gets cleared, which
    is spotted on the next negedge of the clock. With some schedulings
    from the simulator, we only see the ECALL instruction on the following
    posedge, by which time the scoreboard thinks we've stopped execution.
    This causes the check on line 290 of otbn_scoreboard.sv to explode.
    
    Note that there's work afoot to flop the STATUS register. This problem
    will go away anyway when that lands, but it seems cleaner to use a
    clocking block to get rid of the race.
    
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
