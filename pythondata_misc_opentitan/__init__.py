import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12377"
version_tuple = (0, 0, 12377)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12377")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12237"
data_version_tuple = (0, 0, 12237)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12237")
except ImportError:
    pass
data_git_hash = "538c36b83659cd5b9898e3f1b4c94b66a25d4e18"
data_git_describe = "v0.0-12237-g538c36b83"
data_git_msg = """\
commit 538c36b83659cd5b9898e3f1b4c94b66a25d4e18
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri May 20 17:24:24 2022 +0100

    [otbn, dv] Disabling end addr check when zero state error is injected
    
    This commit disables end addr check when zero state error is injected
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
