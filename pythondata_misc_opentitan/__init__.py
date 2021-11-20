import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8799"
version_tuple = (0, 0, 8799)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8799")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8687"
data_version_tuple = (0, 0, 8687)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8687")
except ImportError:
    pass
data_git_hash = "41fc13b60c68eced9eda18b69b3de53db45a8143"
data_git_describe = "v0.0-8687-g41fc13b60"
data_git_msg = """\
commit 41fc13b60c68eced9eda18b69b3de53db45a8143
Author: Weicai Yang <weicai@google.com>
Date:   Fri Nov 19 15:53:33 2021 -0800

    [ci] Fix CI failure
    
    mubi*_e is removed in one PR while the other PR added a new update which
    still used it
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
