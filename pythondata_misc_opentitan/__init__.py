import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5177"
version_tuple = (0, 0, 5177)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5177")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5086"
data_version_tuple = (0, 0, 5086)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5086")
except ImportError:
    pass
data_git_hash = "817c04317ecbd491db24c87054594c36a91391a7"
data_git_describe = "v0.0-5086-g817c04317"
data_git_msg = """\
commit 817c04317ecbd491db24c87054594c36a91391a7
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Feb 26 15:41:38 2021 +0000

    [aon_timer] Add known asserts on outputs
    
    Required for D1 status.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
