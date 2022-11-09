import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15347"
version_tuple = (0, 0, 15347)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15347")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15205"
data_version_tuple = (0, 0, 15205)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15205")
except ImportError:
    pass
data_git_hash = "9ef6ee45d730ac82b6eb5eef44f87251a491c24a"
data_git_describe = "v0.0-15205-g9ef6ee45d7"
data_git_msg = """\
commit 9ef6ee45d730ac82b6eb5eef44f87251a491c24a
Author: Eli Kim <eli@opentitan.org>
Date:   Wed Nov 2 15:55:01 2022 -0700

    [rdc/spid] Waive CSR to PAD retention
    
    When SwRstRsq occurs, chip is in active mode. So no retention functions
    are used. The error can be waived.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
