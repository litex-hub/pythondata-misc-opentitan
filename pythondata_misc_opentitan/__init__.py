import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8356"
version_tuple = (0, 0, 8356)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8356")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8244"
data_version_tuple = (0, 0, 8244)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8244")
except ImportError:
    pass
data_git_hash = "6386c757419ca1cdf24004a1bc830931a827850b"
data_git_describe = "v0.0-8244-g6386c7574"
data_git_msg = """\
commit 6386c757419ca1cdf24004a1bc830931a827850b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 15 15:14:14 2021 +0100

    [otbn] Flop STATUS register
    
    This ensures that the STATUS register switches from IDLE to
    BUSY_EXECUTE at the start of an operation on the same cycle as we zero
    out INSN_CNT.
    
    The STATUS change is also delayed by a cycle at the other end of the
    run. Thus we rename the derived "done" signal in the model from
    done_r_o to done_rr_o, showing that it's now delayed by two cycles.
    
    The only other change is to add an expected stall cycle to the count
    in stats_test.py, since there really is one extra stalled cycle that
    we count.
    
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
