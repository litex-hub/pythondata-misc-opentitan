import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12484"
version_tuple = (0, 0, 12484)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12484")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12342"
data_version_tuple = (0, 0, 12342)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12342")
except ImportError:
    pass
data_git_hash = "57b9b4b59175c1acd4ad706ddcf29a7ba4dc4fda"
data_git_describe = "v0.0-12342-g57b9b4b59"
data_git_msg = """\
commit 57b9b4b59175c1acd4ad706ddcf29a7ba4dc4fda
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 1 08:46:54 2022 -0700

    [rstmgr] Minor lint fix
    
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
