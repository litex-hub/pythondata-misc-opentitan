import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12387"
version_tuple = (0, 0, 12387)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12387")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12247"
data_version_tuple = (0, 0, 12247)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12247")
except ImportError:
    pass
data_git_hash = "d2ab5630b1a07fad31e07c9a7500aacf3cb701c6"
data_git_describe = "v0.0-12247-gd2ab5630b"
data_git_msg = """\
commit d2ab5630b1a07fad31e07c9a7500aacf3cb701c6
Author: Timothy Chen <timothytim@google.com>
Date:   Thu May 26 15:47:04 2022 -0700

    [rstmgr] Address comment from #12890
    
    The consistency check default state does not currently signal an error,
    it creates a situation where a continuous glitch or a
    severed enable/clock to the fsm flops could suppress the error/alert.
    
    This does not seem feasible, but it's better to be safe since it
    has a very low cost.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
