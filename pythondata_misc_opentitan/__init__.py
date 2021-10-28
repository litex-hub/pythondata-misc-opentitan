import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8508"
version_tuple = (0, 0, 8508)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8508")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8396"
data_version_tuple = (0, 0, 8396)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8396")
except ImportError:
    pass
data_git_hash = "09c120f36c06ea5309e6666e75fbbacd71edd41a"
data_git_describe = "v0.0-8396-g09c120f36"
data_git_msg = """\
commit 09c120f36c06ea5309e6666e75fbbacd71edd41a
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Oct 21 14:09:35 2021 -0700

    [top/ast] Add misc input pad
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
