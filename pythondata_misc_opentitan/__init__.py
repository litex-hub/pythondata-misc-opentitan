import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12881"
version_tuple = (0, 0, 12881)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12881")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12739"
data_version_tuple = (0, 0, 12739)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12739")
except ImportError:
    pass
data_git_hash = "2c25678cfeb84d119761766a9dcd053f72f32e80"
data_git_describe = "v0.0-12739-g2c25678cfe"
data_git_msg = """\
commit 2c25678cfeb84d119761766a9dcd053f72f32e80
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Jun 28 12:10:45 2022 -0700

    [chip dv] Cleanup task invoked in func warning
    
    This cleans up tasks invoked in functions warning and promotes it to
    an error. This is not allowed by other tools by default.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
