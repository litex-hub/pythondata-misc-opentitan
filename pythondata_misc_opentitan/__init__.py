import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11073"
version_tuple = (0, 0, 11073)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11073")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10947"
data_version_tuple = (0, 0, 10947)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10947")
except ImportError:
    pass
data_git_hash = "67783a65527f1aaaf937b9ce30866f19816e0205"
data_git_describe = "v0.0-10947-g67783a655"
data_git_msg = """\
commit 67783a65527f1aaaf937b9ce30866f19816e0205
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 18 13:11:07 2022 +0000

    [otbn,rtl] Fix start_stop_control done_o signal when SecWipeEn=0
    
    This single-cycle pulse is supposed to happen at the end of the secure
    wipe. When SecWipeEn=0, we have a single-cycle "secure wipe" that just
    jumps straight to OtbnStartStopSecureWipeComplete. But the done_o
    signal didn't match: fix that.
    
    There's also a corresponding DV change needed to get the status signal
    timing right.
    
    Note that this commit only works with the previous two: we are now
    delaying the "done_core" signal in otbn.sv by a cycle, even when
    secure wipe is disabled.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
