import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11508"
version_tuple = (0, 0, 11508)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11508")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11382"
data_version_tuple = (0, 0, 11382)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11382")
except ImportError:
    pass
data_git_hash = "5e74adddb817de817a5928626d9106eef3ea4cea"
data_git_describe = "v0.0-11382-g5e74adddb"
data_git_msg = """\
commit 5e74adddb817de817a5928626d9106eef3ea4cea
Author: Michael Schaffner <msf@google.com>
Date:   Thu Apr 7 18:57:52 2022 -0700

    [prim_onehot_check] Add prim_onehot_check
    
    Adds a checker module that can be used to check the onehot0 property of
    a vector. This is useful for checks such as spurious write-enable
    detection on CSR and register file blocks (for triggering alerts).
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
