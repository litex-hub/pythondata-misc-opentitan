import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14979"
version_tuple = (0, 0, 14979)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14979")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14837"
data_version_tuple = (0, 0, 14837)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14837")
except ImportError:
    pass
data_git_hash = "f46226d1f3149b49aaf89963b7f7bd02e0eb6ab8"
data_git_describe = "v0.0-14837-gf46226d1f3"
data_git_msg = """\
commit f46226d1f3149b49aaf89963b7f7bd02e0eb6ab8
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Oct 26 16:30:39 2022 -0700

    [top] Reduce async fifo depth
    
    Fix issue identified in #14204
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
