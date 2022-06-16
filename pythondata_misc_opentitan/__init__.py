import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12720"
version_tuple = (0, 0, 12720)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12720")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12578"
data_version_tuple = (0, 0, 12578)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12578")
except ImportError:
    pass
data_git_hash = "a1c71d4ebfa2d1881234551efc7f7cb1c6b3e23d"
data_git_describe = "v0.0-12578-ga1c71d4eb"
data_git_msg = """\
commit a1c71d4ebfa2d1881234551efc7f7cb1c6b3e23d
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Jun 15 12:45:09 2022 +0100

    [doc] Add documentation for OTBN build artifacts.
    
    Add a description of what kind of Bazel artifacts are produced by the
    OTBN build flow, and a little guidance on how to use them.
    
    Resolves a TODO from the recent Bazel docs push.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
