import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12358"
version_tuple = (0, 0, 12358)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12358")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12218"
data_version_tuple = (0, 0, 12218)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12218")
except ImportError:
    pass
data_git_hash = "cd679fd9e7da1a85a343b6aaeae80e8a3f1f92a0"
data_git_describe = "v0.0-12218-gcd679fd9e"
data_git_msg = """\
commit cd679fd9e7da1a85a343b6aaeae80e8a3f1f92a0
Author: Michael Schaffner <msf@google.com>
Date:   Wed May 25 16:14:18 2022 -0700

    Revert "[python] Bump fusesoc/edalize versions"
    
    This reverts commit 8339519c379ad270bd2a091522ec564b08ebc41e.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
