import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12477"
version_tuple = (0, 0, 12477)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12477")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12335"
data_version_tuple = (0, 0, 12335)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12335")
except ImportError:
    pass
data_git_hash = "c48bdec44d6abdf1214951fe68c815c0b3af8d43"
data_git_describe = "v0.0-12335-gc48bdec44"
data_git_msg = """\
commit c48bdec44d6abdf1214951fe68c815c0b3af8d43
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jun 1 16:58:06 2022 -0700

    [dv] Remove 2 cycle delay after injecting the fault
    
    Addess #12990
    Signed-off-by: Weicai Yang <weicai@google.com>

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
