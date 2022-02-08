import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10129"
version_tuple = (0, 0, 10129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10005"
data_version_tuple = (0, 0, 10005)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10005")
except ImportError:
    pass
data_git_hash = "0fad9274ebb110c755db2fa936aab0baf422c21c"
data_git_describe = "v0.0-10005-g0fad9274e"
data_git_msg = """\
commit 0fad9274ebb110c755db2fa936aab0baf422c21c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 3 07:52:41 2022 +0000

    [otbn,dv] Fix assertion in RND FSM checking
    
    If we are prefetching and a response comes in from the
    EDN (edn_rnd_ack_i) at the same time as an instruction reads from
    RND (rnd_req_i), we go to the "full" state, not the "reading" state.
    
    The FSM I'd sketched out in the assertions was bogus: when both of
    those signals are asserted at the same time, we can't go into both
    READING and FULL states!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
