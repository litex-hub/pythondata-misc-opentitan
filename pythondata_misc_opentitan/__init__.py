import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14793"
version_tuple = (0, 0, 14793)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14793")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14651"
data_version_tuple = (0, 0, 14651)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14651")
except ImportError:
    pass
data_git_hash = "4b867c56f4dc553d78485e6b4192d48ef4c72892"
data_git_describe = "v0.0-14651-g4b867c56f4"
data_git_msg = """\
commit 4b867c56f4dc553d78485e6b4192d48ef4c72892
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Oct 17 12:45:02 2022 -0700

    [top/dv] Automatically backdoor load ROM_EXEC_EN
    
    This is the same fix as the one applied to lc_walkthrough.
    
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
