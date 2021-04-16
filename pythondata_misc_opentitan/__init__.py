import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5890"
version_tuple = (0, 0, 5890)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5890")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5795"
data_version_tuple = (0, 0, 5795)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5795")
except ImportError:
    pass
data_git_hash = "53b946bbb6c87072d6f57697155f56fd41372a4b"
data_git_describe = "v0.0-5795-g53b946bbb"
data_git_msg = """\
commit 53b946bbb6c87072d6f57697155f56fd41372a4b
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Apr 15 12:27:57 2021 -0700

    [topgen] Fix enum type warnings
    
    enum for top package did not define any type. Change them to `int
    unsigned`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
