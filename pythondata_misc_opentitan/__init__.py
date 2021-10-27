import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8465"
version_tuple = (0, 0, 8465)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8465")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8353"
data_version_tuple = (0, 0, 8353)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8353")
except ImportError:
    pass
data_git_hash = "0b03e6a6ada95c9d3fc04d50a01a35a59d3d4e40"
data_git_describe = "v0.0-8353-g0b03e6a6a"
data_git_msg = """\
commit 0b03e6a6ada95c9d3fc04d50a01a35a59d3d4e40
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Tue Oct 26 11:05:23 2021 -0700

    [test/ci] Disable Silicon Creator tests
    
    The current silicon creator tests don't support ROM_EXT signature
    verification. This commit disables the tests from CI and from
    systemtest until lowrisc/opentitan#8902 is resolved.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
