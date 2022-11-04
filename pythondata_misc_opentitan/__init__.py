import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15235"
version_tuple = (0, 0, 15235)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15235")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15093"
data_version_tuple = (0, 0, 15093)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15093")
except ImportError:
    pass
data_git_hash = "a7232b56cac7f415c3ed0acdace2ca6e3b92c61b"
data_git_describe = "v0.0-15093-ga7232b56ca"
data_git_msg = """\
commit a7232b56cac7f415c3ed0acdace2ca6e3b92c61b
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Nov 3 16:37:30 2022 -0400

    [doc] Add skip_in_ci tag to build_sw.md
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
