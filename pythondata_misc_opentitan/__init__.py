import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10726"
version_tuple = (0, 0, 10726)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10726")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10600"
data_version_tuple = (0, 0, 10600)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10600")
except ImportError:
    pass
data_git_hash = "4e0e44a3c86943209c7002d2b54aac0821c89a3d"
data_git_describe = "v0.0-10600-g4e0e44a3c"
data_git_msg = """\
commit 4e0e44a3c86943209c7002d2b54aac0821c89a3d
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Mar 2 15:13:58 2022 -0800

    [pinmux] Update docs
    
    Fix #11194
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
