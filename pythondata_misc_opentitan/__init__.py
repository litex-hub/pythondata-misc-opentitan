import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10224"
version_tuple = (0, 0, 10224)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10224")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10100"
data_version_tuple = (0, 0, 10100)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10100")
except ImportError:
    pass
data_git_hash = "018dac54829f0309e6cd215f63e670c933e3fa6e"
data_git_describe = "v0.0-10100-g018dac548"
data_git_msg = """\
commit 018dac54829f0309e6cd215f63e670c933e3fa6e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 3 11:31:46 2022 +0000

    [otbn,dv] Properly represent DMEM store latency in ISS
    
    This wouldn't matter except that we want to support a test where we
    invalidate the whole of DMEM (to trigger integrity errors) at some
    arbitrary point in the run.
    
    If we're unlucky and happen to do this just after executing a store
    then the RTL will apply the store on the following cycle (leaving
    valid integrity bits) but the ISS, which had applied the store
    already, would mark the location as having bad integrity.
    
    The correct fix is easy enough: keep an extra "pending" queue that
    only gets applied on the following cycle.
    
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
