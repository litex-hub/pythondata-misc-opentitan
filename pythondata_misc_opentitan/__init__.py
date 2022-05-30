import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12406"
version_tuple = (0, 0, 12406)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12406")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12266"
data_version_tuple = (0, 0, 12266)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12266")
except ImportError:
    pass
data_git_hash = "78e9223cdcbe9921f22c8b95dc5e1ae41c01ccc7"
data_git_describe = "v0.0-12266-g78e9223cd"
data_git_msg = """\
commit 78e9223cdcbe9921f22c8b95dc5e1ae41c01ccc7
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Thu Apr 21 03:32:22 2022 -0700

    [aes/dv] implemented fault inject into aes_control_fsm
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
