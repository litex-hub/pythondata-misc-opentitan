import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12908"
version_tuple = (0, 0, 12908)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12908")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12766"
data_version_tuple = (0, 0, 12766)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12766")
except ImportError:
    pass
data_git_hash = "6f314fc6c54188f704bc3b68be4cd1d1a7350ea8"
data_git_describe = "v0.0-12766-g6f314fc6c5"
data_git_msg = """\
commit 6f314fc6c54188f704bc3b68be4cd1d1a7350ea8
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Jun 16 15:37:41 2022 -0700

    [doc] Update top earlgrey specification.
    
    Partial description updates, integration of Hugo memory map and pinout
    shortcodes.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
