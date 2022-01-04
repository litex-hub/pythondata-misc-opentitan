import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9314"
version_tuple = (0, 0, 9314)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9314")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9197"
data_version_tuple = (0, 0, 9197)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9197")
except ImportError:
    pass
data_git_hash = "fafeaf223e11aa36e33606b9aadca4cd6b175863"
data_git_describe = "v0.0-9197-gfafeaf223"
data_git_msg = """\
commit fafeaf223e11aa36e33606b9aadca4cd6b175863
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 4 14:42:44 2022 +0000

    [otbn] Widen prefetch_loop_end_addr to avoid overflow
    
    There's an amusing bug that you can trigger if you have something like
    
       loopi  123, 1025
    
    The problem is that 1025 instructions (the loop body length) works out
    as 4096 + 4 bytes, so the correct value of prefetch_loop_end_addr is
    something like old_addr + 4096 + 4.
    
    Unfortunately, 4096 is the size of IMEM so we were truncating this to
    just old_addr + 4. This meant that the prefetch stage thought that the
    following instruction was at the end of the loop and predicted a back
    edge. Eventually, we failed the NoAddressMismatch assertion in
    otbn_instruction_fetch.sv.
    
    The fix is to pass one extra bit in the address, just like we already
    do with the check in the loop controller itself.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
