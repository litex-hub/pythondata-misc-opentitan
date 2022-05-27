import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12371"
version_tuple = (0, 0, 12371)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12371")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12231"
data_version_tuple = (0, 0, 12231)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12231")
except ImportError:
    pass
data_git_hash = "757a768cc8d9395c49ec8479f5aed45a574d2c54"
data_git_describe = "v0.0-12231-g757a768cc"
data_git_msg = """\
commit 757a768cc8d9395c49ec8479f5aed45a574d2c54
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed May 18 14:33:17 2022 +0100

    [otbn, rtl] Add fatal error when prefetch isn't correct
    
    By design the prefetch stage either prefetches the correct address or
    doesn't prefetch. If a prefetched instruction has a different address to
    the one required by the instruction fetch stage a fault has ocurred.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
