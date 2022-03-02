import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10639"
version_tuple = (0, 0, 10639)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10639")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10513"
data_version_tuple = (0, 0, 10513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10513")
except ImportError:
    pass
data_git_hash = "c0b2772f39876dd924bf1a33a120cadc5d52e40a"
data_git_describe = "v0.0-10513-gc0b2772f3"
data_git_msg = """\
commit c0b2772f39876dd924bf1a33a120cadc5d52e40a
Author: Michael Schaffner <msf@google.com>
Date:   Tue Feb 22 17:56:42 2022 -0800

    [dv] Flag illegal ENUMASSIGN warnings as errors
    
    Illegal ENUM assignments can cause LEC warnings later down the road.
    The warning is therefore promoted to an error in simulations in
    order to catch this as early as possible.
    
    See #10083, #10952 for context.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
