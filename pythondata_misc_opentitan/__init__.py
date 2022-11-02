import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15147"
version_tuple = (0, 0, 15147)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15147")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15005"
data_version_tuple = (0, 0, 15005)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15005")
except ImportError:
    pass
data_git_hash = "0b93f44c7a87e83cbc919b88c0ff907178bd43ec"
data_git_describe = "v0.0-15005-g0b93f44c7a"
data_git_msg = """\
commit 0b93f44c7a87e83cbc919b88c0ff907178bd43ec
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Nov 2 13:32:30 2022 -0700

    [bazel] rollback 15905 to triage Bazel airgapped issues
    
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
