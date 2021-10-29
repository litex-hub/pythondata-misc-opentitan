import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8515"
version_tuple = (0, 0, 8515)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8515")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8403"
data_version_tuple = (0, 0, 8403)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8403")
except ImportError:
    pass
data_git_hash = "419ccddfc52dee678d9964c3aa6d41d0dc9017d0"
data_git_describe = "v0.0-8403-g419ccddfc"
data_git_msg = """\
commit 419ccddfc52dee678d9964c3aa6d41d0dc9017d0
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 28 16:50:30 2021 +0100

    [prim] Tweak prim_sync_reqack_data assertion so it can be disabled
    
    When we run $assertoff(), it stops any new assertion sequences from
    being started. However, this part of the previous assertion:
    
        $stable(data_o) [*2]
    
    consumed time. If we inject a reset on the DST side that causes the
    value to change in the last cycle of the window, an $assertoff won't
    save us because the assertion that started on the previous cycle will
    still run to completion.
    
    Unfold the $stable(..) calls into comparisons between $past() and
    present and change the assertion so that it doesn't consume time,
    allowing it to be disabled at any point.
    
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
