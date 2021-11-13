import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8712"
version_tuple = (0, 0, 8712)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8712")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8600"
data_version_tuple = (0, 0, 8600)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8600")
except ImportError:
    pass
data_git_hash = "4c0e61fd2ee6cbca3fb59e0c542409b53aeac606"
data_git_describe = "v0.0-8600-g4c0e61fd2"
data_git_msg = """\
commit 4c0e61fd2ee6cbca3fb59e0c542409b53aeac606
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Nov 11 14:32:53 2021 -0800

    [util] Add alternate hjson paths for reggen_only modules
    
    - Fixes #8207
    
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
