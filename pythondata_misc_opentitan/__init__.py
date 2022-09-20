import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14299"
version_tuple = (0, 0, 14299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14157"
data_version_tuple = (0, 0, 14157)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14157")
except ImportError:
    pass
data_git_hash = "d78041711d5d2d8f8782151cb13d8cc40d35c8d5"
data_git_describe = "v0.0-14157-gd78041711d"
data_git_msg = """\
commit d78041711d5d2d8f8782151cb13d8cc40d35c8d5
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Mon Sep 19 16:13:35 2022 +0100

    [COMMITTERS] Make Jaedon Kim and Drew Macrae committers
    
    Jaedon and Drew have been made committers by the Technical
    Committee. Thanks for your contributions!
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
