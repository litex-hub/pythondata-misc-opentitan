import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12925"
version_tuple = (0, 0, 12925)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12925")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12783"
data_version_tuple = (0, 0, 12783)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12783")
except ImportError:
    pass
data_git_hash = "1697525a0b9029af2a8601be5bfecb9449f3492d"
data_git_describe = "v0.0-12783-g1697525a0b"
data_git_msg = """\
commit 1697525a0b9029af2a8601be5bfecb9449f3492d
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Jul 1 10:09:49 2022 -0700

    [doc] Remove sw/device/examples index page.
    
    This document currently doesn't have any content, and all examples
    documentation are covered in README.md files.
    
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
