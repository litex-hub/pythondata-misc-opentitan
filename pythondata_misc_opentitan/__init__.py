import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12966"
version_tuple = (0, 0, 12966)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12966")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12824"
data_version_tuple = (0, 0, 12824)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12824")
except ImportError:
    pass
data_git_hash = "6b85dcae41936ffb61d2ac8c6bf3f590a751c408"
data_git_describe = "v0.0-12824-g6b85dcae41"
data_git_msg = """\
commit 6b85dcae41936ffb61d2ac8c6bf3f590a751c408
Author: Alexander Williams <awill@google.com>
Date:   Thu Jul 7 08:43:12 2022 -0700

    [sw] Remove unused flash_ctrl build target
    
    The code was removed, but the build target remained and refers to
    nonexistent files.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
