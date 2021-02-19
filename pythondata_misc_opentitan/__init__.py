import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5053"
version_tuple = (0, 0, 5053)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5053")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4962"
data_version_tuple = (0, 0, 4962)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4962")
except ImportError:
    pass
data_git_hash = "f2a373a70fd3e76fbb6ba3b1b9df0d33674b1697"
data_git_describe = "v0.0-4962-gf2a373a70"
data_git_msg = """\
commit f2a373a70fd3e76fbb6ba3b1b9df0d33674b1697
Author: Tobias Wölfel <tobias.woelfel@mailbox.org>
Date:   Thu Feb 18 22:42:28 2021 +0100

    Fix spelling errors
    
    Signed-off-by: Tobias Wölfel <tobias.woelfel@mailbox.org>

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
