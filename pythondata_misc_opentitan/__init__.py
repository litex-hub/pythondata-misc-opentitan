import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12423"
version_tuple = (0, 0, 12423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12281"
data_version_tuple = (0, 0, 12281)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12281")
except ImportError:
    pass
data_git_hash = "6b5814b85d9b6c86d1ab99a90bee539e5780be22"
data_git_describe = "v0.0-12281-g6b5814b85"
data_git_msg = """\
commit 6b5814b85d9b6c86d1ab99a90bee539e5780be22
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu May 26 11:18:48 2022 +0100

    [dif, ibex] Add nmi api with unittests
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
