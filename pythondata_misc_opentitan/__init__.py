import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10330"
version_tuple = (0, 0, 10330)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10330")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10204"
data_version_tuple = (0, 0, 10204)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10204")
except ImportError:
    pass
data_git_hash = "a48e5e162aa7a04fc47e4fab6866f0126567bf77"
data_git_describe = "v0.0-10204-ga48e5e162"
data_git_msg = """\
commit a48e5e162aa7a04fc47e4fab6866f0126567bf77
Author: Alexander Williams <awill@google.com>
Date:   Mon Feb 14 16:20:47 2022 -0800

    [usbdev] Clean up headers and validate num EPs
    
    The number of IN endpoints and number of OUT endpoints must be equal for
    the current code.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
