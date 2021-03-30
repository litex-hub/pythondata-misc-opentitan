import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5637"
version_tuple = (0, 0, 5637)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5637")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5542"
data_version_tuple = (0, 0, 5542)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5542")
except ImportError:
    pass
data_git_hash = "ee472e9f0c70126004d433c9c2b4ab05f4528b38"
data_git_describe = "v0.0-5542-gee472e9f0"
data_git_msg = """\
commit ee472e9f0c70126004d433c9c2b4ab05f4528b38
Author: Weicai Yang <weicai@google.com>
Date:   Tue Mar 23 22:46:26 2021 -0700

    [dv] Fix reg backdoor
    
    3 fixes in this PR
    1. Fix hier_path not used in top reg
    2. Fix path check didn't run properly as path types weren't given
    3. Fix wrong error message `does not have hdl path defined for
    abstraction 'RTL'`, we don't use `RTL` as hdl path, it should be
    `BkdrRegPathRtl`
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
