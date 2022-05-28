import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12396"
version_tuple = (0, 0, 12396)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12396")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12256"
data_version_tuple = (0, 0, 12256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12256")
except ImportError:
    pass
data_git_hash = "2e9cc9f72d6d1d39d6c68e68f2d3ab7d0f7fba39"
data_git_describe = "v0.0-12256-g2e9cc9f72"
data_git_msg = """\
commit 2e9cc9f72d6d1d39d6c68e68f2d3ab7d0f7fba39
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri May 27 12:41:15 2022 -0700

    [sw/tests] update non-volatile flash region example
    
    The non-volatile flash region example did not make it clear that any
    non-volatile flash data should be initialized to all 1s to achieve the
    desired behavior.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
