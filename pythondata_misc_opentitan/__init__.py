import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10387"
version_tuple = (0, 0, 10387)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10387")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10261"
data_version_tuple = (0, 0, 10261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10261")
except ImportError:
    pass
data_git_hash = "e1292d6a93f6b7d64c76bff8ff4597b80764520a"
data_git_describe = "v0.0-10261-ge1292d6a9"
data_git_msg = """\
commit e1292d6a93f6b7d64c76bff8ff4597b80764520a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 14 22:50:59 2022 +0000

    [otbn,dv] Include pending stores in ISS DMEM dumps
    
    This matches the timing that we see on the RTL side, fixing
    some (honestly very confusing!) mismatches that came up in a stress
    test.
    
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
