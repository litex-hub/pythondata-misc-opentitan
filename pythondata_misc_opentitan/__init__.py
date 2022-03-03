import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10675"
version_tuple = (0, 0, 10675)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10675")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10549"
data_version_tuple = (0, 0, 10549)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10549")
except ImportError:
    pass
data_git_hash = "0d0fa1a09f8f43b697a8f0600325acce8d1a2751"
data_git_describe = "v0.0-10549-g0d0fa1a09"
data_git_msg = """\
commit 0d0fa1a09f8f43b697a8f0600325acce8d1a2751
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 1 16:30:40 2022 +0000

    [otbn,dv] Remove support for the model in the OTBN module
    
    This was originally put in so that we could do system-level testing of
    OTBN before the implementation was complete. Since then, it has been
    used once or twice for performance tests where we needed to model the
    Ibex side as well. But it's really rather difficult to maintain, and
    leaves a bit of "DV-ish" code in the design folder.
    
    If we need to do something like this in future, it shouldn't be too
    hard to knock together another frontend to the simulator (like
    stepped.sv) and to build a testbench in Python.
    
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
