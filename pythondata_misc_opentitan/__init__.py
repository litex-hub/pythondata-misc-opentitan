import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9514"
version_tuple = (0, 0, 9514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9394"
data_version_tuple = (0, 0, 9394)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9394")
except ImportError:
    pass
data_git_hash = "e4c5d706cc9d6516a58dd271485f7eee1b91cf7e"
data_git_describe = "v0.0-9394-ge4c5d706c"
data_git_msg = """\
commit e4c5d706cc9d6516a58dd271485f7eee1b91cf7e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jan 11 16:25:32 2022 -0500

    [bazel] Update BUILD files
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post120"
tool_version_tuple = (0, 0, 120)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post120")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
