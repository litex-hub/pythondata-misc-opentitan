import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9860"
version_tuple = (0, 0, 9860)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9860")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9736"
data_version_tuple = (0, 0, 9736)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9736")
except ImportError:
    pass
data_git_hash = "968524e4b9dff05b8b23191890c21ea9a02dd032"
data_git_describe = "v0.0-9736-g968524e4b"
data_git_msg = """\
commit 968524e4b9dff05b8b23191890c21ea9a02dd032
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Jan 10 16:20:20 2022 -0500

    [opentitantool] Add sha256
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
