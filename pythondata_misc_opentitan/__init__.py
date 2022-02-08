import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10157"
version_tuple = (0, 0, 10157)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10157")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10033"
data_version_tuple = (0, 0, 10033)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10033")
except ImportError:
    pass
data_git_hash = "09b10ba9937cf6d502d4a9a726b51784265b04f1"
data_git_describe = "v0.0-10033-g09b10ba99"
data_git_msg = """\
commit 09b10ba9937cf6d502d4a9a726b51784265b04f1
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 8 10:36:45 2022 -0800

    [prim] Add stub flops to remove lint warnings
    
    - for prim_mubi_sync/sender modules, when the AsynOn option is 0, the clk/rst_n inputs are used only for assertions.
    - this causes the lint tools to throw a CLOCK_USE error as there are no valid loads on the clock.
    - this commit adds unused stub logic that makes use of the clock and removes the lint error without having to add to individual waiver files.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
