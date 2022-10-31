import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15068"
version_tuple = (0, 0, 15068)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15068")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14926"
data_version_tuple = (0, 0, 14926)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14926")
except ImportError:
    pass
data_git_hash = "27b97cb8f39298901bf61226a559aa91980cf958"
data_git_describe = "v0.0-14926-g27b97cb8f3"
data_git_msg = """\
commit 27b97cb8f39298901bf61226a559aa91980cf958
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Oct 28 19:11:53 2022 -0700

    [edn] Refactor edn_enable_fanout
    
    Convert to use enum so that future changes do not need
    to shift bits.
    
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
