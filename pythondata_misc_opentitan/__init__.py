import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9448"
version_tuple = (0, 0, 9448)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9448")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9330"
data_version_tuple = (0, 0, 9330)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9330")
except ImportError:
    pass
data_git_hash = "e40b42973f1410008feb98aeac2376d30656010c"
data_git_describe = "v0.0-9330-ge40b42973"
data_git_msg = """\
commit e40b42973f1410008feb98aeac2376d30656010c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 11 16:29:44 2022 +0000

    [otbn,dv] Avoid "double recov alert" problem
    
    Some sequences of operations could cause a problem where we ran two
    back-to-back operations, each of which causing a recoverable alert,
    where the second operation finished while before the handshake of the
    first alert finished. If this happened, we would essentially drop the
    second alert, causing the scoreboard to complain.
    
    The fix is to expose the "waiting for an alert" state from the
    scoreboard and wait in the vseq for that, then for any following
    recoverable alert handshake to finish. This way, we can't start the
    second operation too early.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
