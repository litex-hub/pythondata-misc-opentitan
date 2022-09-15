import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14218"
version_tuple = (0, 0, 14218)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14218")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14076"
data_version_tuple = (0, 0, 14076)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14076")
except ImportError:
    pass
data_git_hash = "490b9d86df769ffb6d0efd8e637904c1a7aa792c"
data_git_describe = "v0.0-14076-g490b9d86df"
data_git_msg = """\
commit 490b9d86df769ffb6d0efd8e637904c1a7aa792c
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 17:59:32 2022 -0700

    [bazel] rollback #14924 and #14927
    
    Since #14860 was rolled back, #14924 and #14927 should also be rolled
    back since they were fixes in response to #14860 to begin with.
    
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
