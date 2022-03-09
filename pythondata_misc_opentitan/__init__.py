import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10791"
version_tuple = (0, 0, 10791)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10791")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10665"
data_version_tuple = (0, 0, 10665)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10665")
except ImportError:
    pass
data_git_hash = "e5b4eda44e53a5950716a3993d397d5374f1af95"
data_git_describe = "v0.0-10665-ge5b4eda44"
data_git_msg = """\
commit e5b4eda44e53a5950716a3993d397d5374f1af95
Author: Weicai Yang <weicai@google.com>
Date:   Tue Mar 8 15:51:00 2022 -0800

    [dv] Update checklist for all blocks
    
    A follow-up update for #11053
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
