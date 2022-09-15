import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14209"
version_tuple = (0, 0, 14209)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14209")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14067"
data_version_tuple = (0, 0, 14067)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14067")
except ImportError:
    pass
data_git_hash = "28f79af3c25d17cee70597881b6b8ba0fa0fc434"
data_git_describe = "v0.0-14067-g28f79af3c2"
data_git_msg = """\
commit 28f79af3c25d17cee70597881b6b8ba0fa0fc434
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 16:36:53 2022 -0700

    [bazel,ottool] rollback #14860
    
    PR #14860 is causing issues in the airgapped environment so temporarily
    rolling back.
    
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
