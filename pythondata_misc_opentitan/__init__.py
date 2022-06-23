import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12795"
version_tuple = (0, 0, 12795)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12795")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12653"
data_version_tuple = (0, 0, 12653)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12653")
except ImportError:
    pass
data_git_hash = "29f760ca206ba7e6f163934acb294e6e40f75e72"
data_git_describe = "v0.0-12653-g29f760ca20"
data_git_msg = """\
commit 29f760ca206ba7e6f163934acb294e6e40f75e72
Author: Timothy Chen <timothytim@google.com>
Date:   Thu May 19 14:38:15 2022 -0700

    [top] Auto generate
    
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
