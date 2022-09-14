import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14200"
version_tuple = (0, 0, 14200)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14200")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14058"
data_version_tuple = (0, 0, 14058)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14058")
except ImportError:
    pass
data_git_hash = "6a9a3e310765253a6c033b0910c13533a2410a26"
data_git_describe = "v0.0-14058-g6a9a3e3107"
data_git_msg = """\
commit 6a9a3e310765253a6c033b0910c13533a2410a26
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 13:12:55 2022 -0700

    [bazel] fix bazel airgapped prep script
    
    PR #14924 should have also added another dep to the airgapped script.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
