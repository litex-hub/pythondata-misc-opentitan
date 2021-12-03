import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8983"
version_tuple = (0, 0, 8983)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8983")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8871"
data_version_tuple = (0, 0, 8871)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8871")
except ImportError:
    pass
data_git_hash = "8adc6a53f743f670cb100890722dfa14803912ba"
data_git_describe = "v0.0-8871-g8adc6a53f"
data_git_msg = """\
commit 8adc6a53f743f670cb100890722dfa14803912ba
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Fri Dec 3 07:16:07 2021 -0800

    [sideload] fixed sideload if
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
