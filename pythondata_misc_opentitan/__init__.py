import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15164"
version_tuple = (0, 0, 15164)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15164")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15022"
data_version_tuple = (0, 0, 15022)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15022")
except ImportError:
    pass
data_git_hash = "36f0619185e9a8e5dfd1dd94dc4a608c6d2a874a"
data_git_describe = "v0.0-15022-g36f0619185"
data_git_msg = """\
commit 36f0619185e9a8e5dfd1dd94dc4a608c6d2a874a
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Oct 31 16:58:46 2022 -0700

    [dv/cdc] Use cycle based CDC instrumentation
    
    This changes the DCD instrumentation to be cycle-based, randomly adding an
    extra cycle in the inputs to the first flop in prim_flop_2sync, replacing
    the time-delay instrumentation.
    
    Fixes #15768
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
