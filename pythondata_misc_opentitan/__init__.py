import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8417"
version_tuple = (0, 0, 8417)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8417")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8305"
data_version_tuple = (0, 0, 8305)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8305")
except ImportError:
    pass
data_git_hash = "0046b1e5f3044fe926016f93896f4888b8cae210"
data_git_describe = "v0.0-8305-g0046b1e5f"
data_git_msg = """\
commit 0046b1e5f3044fe926016f93896f4888b8cae210
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 21 15:38:29 2021 -0700

    [dv] Fix scb multi-ral
    
    2 places still use `ral` rather than `ral_models[name]`
    
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
