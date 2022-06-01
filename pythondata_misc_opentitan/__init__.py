import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12444"
version_tuple = (0, 0, 12444)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12444")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12302"
data_version_tuple = (0, 0, 12302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12302")
except ImportError:
    pass
data_git_hash = "4f6eadba989c3712df79e23880d462192d48a24f"
data_git_describe = "v0.0-12302-g4f6eadba9"
data_git_msg = """\
commit 4f6eadba989c3712df79e23880d462192d48a24f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri May 27 17:56:24 2022 +0100

    [otbn,rtl] Squash prefetch mismatch error when controller stops
    
    Without this squashing behaviour, there's a problem if the controller
    stops on an instruction that doesn't look like a jump/branch/etc. This
    stalls the instruction stream (so insn_fetch_req_addr_i stops
    changing). In this case, the invalid instruction didn't look like a
    jump or similar, so the prefetcher has already been incremented by 4.
    We then generate an error (insn_addr_err_o) when we look at the
    results.
    
    Hopefully, any situation like this would be caught by the existing
    testbench (by looking at ERR_BITS). But we definitely catch situations
    where the initial error is only supposed to send out a recoverable
    alert. In this case, the testbench notices that an unexpected fatal
    alert came out.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
