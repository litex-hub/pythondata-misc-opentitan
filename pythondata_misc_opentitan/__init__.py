import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12797"
version_tuple = (0, 0, 12797)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12797")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12655"
data_version_tuple = (0, 0, 12655)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12655")
except ImportError:
    pass
data_git_hash = "85d5126183fae9084c9626d890d76b7859d9d89e"
data_git_describe = "v0.0-12655-g85d5126183"
data_git_msg = """\
commit 85d5126183fae9084c9626d890d76b7859d9d89e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 11 12:19:58 2022 +0000

    [otbn] Remove SecWipeEn configuration machinery
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
