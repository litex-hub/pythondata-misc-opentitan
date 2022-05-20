import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12253"
version_tuple = (0, 0, 12253)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12253")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12125"
data_version_tuple = (0, 0, 12125)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12125")
except ImportError:
    pass
data_git_hash = "3024b9b2178c4994935cfdfa8179158f5e2ebabd"
data_git_describe = "v0.0-12125-g3024b9b21"
data_git_msg = """\
commit 3024b9b2178c4994935cfdfa8179158f5e2ebabd
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu May 19 12:11:52 2022 -0400

    [bazel] bitstreams don't refresh when offline
    
    and added latest.txt
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
