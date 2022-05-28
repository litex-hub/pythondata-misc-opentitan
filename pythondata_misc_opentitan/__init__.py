import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12399"
version_tuple = (0, 0, 12399)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12399")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12259"
data_version_tuple = (0, 0, 12259)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12259")
except ImportError:
    pass
data_git_hash = "5bba2ebc2d8893fee484129cf148f906d88f7a4a"
data_git_describe = "v0.0-12259-g5bba2ebc2"
data_git_msg = """\
commit 5bba2ebc2d8893fee484129cf148f906d88f7a4a
Author: Alexander Williams <awill@google.com>
Date:   Fri May 27 16:24:15 2022 -0700

    [top] Autogenerate
    
    Autogenerate with fixed whitespace.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
