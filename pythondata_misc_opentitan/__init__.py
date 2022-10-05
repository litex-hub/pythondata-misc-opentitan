import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14558"
version_tuple = (0, 0, 14558)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14558")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14416"
data_version_tuple = (0, 0, 14416)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14416")
except ImportError:
    pass
data_git_hash = "5220e2275b3bae33225cc77dbc48b839ebd3ef29"
data_git_describe = "v0.0-14416-g5220e2275b"
data_git_msg = """\
commit 5220e2275b3bae33225cc77dbc48b839ebd3ef29
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Oct 4 17:40:19 2022 -0700

    [top/dv] Fix rstmgr info test
    
    Previously, this test assumed that escalation would always happen
    within a fixed amount of time.  However, that is not necessarily
    the case for ping timeouts.  The ping mechanism randomly selects a
    peripheral to check.  However, since the selection vector is larger
    than the number of peripherals we have, it does not always select a valid
    peripheral. When the alert handler does not select a valid peripheral,
    it simply moves on to the test the next ping. However the max wait time
    until the next ping is checked is in the mS range.
    Therefore, the test should not make that assumption and just wait in
    place.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
