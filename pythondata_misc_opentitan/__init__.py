import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10308"
version_tuple = (0, 0, 10308)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10308")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10182"
data_version_tuple = (0, 0, 10182)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10182")
except ImportError:
    pass
data_git_hash = "b1e181b4ff83e60f4ee3a567bf358721d5336ad8"
data_git_describe = "v0.0-10182-gb1e181b4f"
data_git_msg = """\
commit b1e181b4ff83e60f4ee3a567bf358721d5336ad8
Author: Alexander Williams <awill@google.com>
Date:   Mon Feb 14 06:53:27 2022 -0800

    [usbdev] Remove unused qe bits in usbctrl reg
    
    These were causing linter warnings, as they were unread.
    
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
