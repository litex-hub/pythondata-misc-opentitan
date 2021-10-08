import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8188"
version_tuple = (0, 0, 8188)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8188")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8076"
data_version_tuple = (0, 0, 8076)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8076")
except ImportError:
    pass
data_git_hash = "9abebb87612201148ab07e754df8802ed2b0ff66"
data_git_describe = "v0.0-8076-g9abebb876"
data_git_msg = """\
commit 9abebb87612201148ab07e754df8802ed2b0ff66
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 7 10:34:11 2021 -0700

    [clkmgr] Update measurement errors to request alerts only once
    
    - previously alerts were requested until software explicitly cleared, but
      this was deemed unacceptable behavior.
    
    - Fixes #8556
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
