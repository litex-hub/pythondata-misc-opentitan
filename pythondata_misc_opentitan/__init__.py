import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13238"
version_tuple = (0, 0, 13238)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13238")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13096"
data_version_tuple = (0, 0, 13096)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13096")
except ImportError:
    pass
data_git_hash = "0ec2d3cbf25b413e0a6ad2fc4b4bbb1715336a43"
data_git_describe = "v0.0-13096-g0ec2d3cbf2"
data_git_msg = """\
commit 0ec2d3cbf25b413e0a6ad2fc4b4bbb1715336a43
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Tue Jul 19 12:00:25 2022 +0200

    [dv/verilator] Fix numeric base of simulation statistics
    
    Prior to this commit, integer simulation statistics, such as the number
    of executed cycles or the size of the trace file, were printed as
    hexadecimal numbers.  Since these numbers are intended for humans, this
    makes little sense.  This commit changes the base of those numbers to
    decimal.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
