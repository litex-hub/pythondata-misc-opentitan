import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14875"
version_tuple = (0, 0, 14875)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14875")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14733"
data_version_tuple = (0, 0, 14733)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14733")
except ImportError:
    pass
data_git_hash = "938687bba3afcf236488299fb31ed036df450102"
data_git_describe = "v0.0-14733-g938687bba3"
data_git_msg = """\
commit 938687bba3afcf236488299fb31ed036df450102
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Oct 18 17:50:23 2022 +0100

    [dv] Fix race condition in otbn_escalate_if
    
    Previously this interface used blocking assignment to set these. This
    led to the updates happening in the wrong place in the simulation
    scheduler. In particular it led to the failure of the `OutputDelay_A`
    assertion in prim_lc_sync in some cases.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
