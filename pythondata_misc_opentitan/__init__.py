import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5014"
version_tuple = (0, 0, 5014)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5014")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4923"
data_version_tuple = (0, 0, 4923)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4923")
except ImportError:
    pass
data_git_hash = "acde96f378b9412ce7919737f11ec0614f03cb8a"
data_git_describe = "v0.0-4923-gacde96f37"
data_git_msg = """\
commit acde96f378b9412ce7919737f11ec0614f03cb8a
Author: Weicai Yang <weicai@google.com>
Date:   Fri Feb 12 13:41:05 2021 -0800

    [keymgr/dv] add lc_disable into stress_all
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
