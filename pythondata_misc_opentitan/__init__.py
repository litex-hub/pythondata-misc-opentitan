import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10299"
version_tuple = (0, 0, 10299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10173"
data_version_tuple = (0, 0, 10173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10173")
except ImportError:
    pass
data_git_hash = "37674c060e3658e035fab8901641344fb1a16741"
data_git_describe = "v0.0-10173-g37674c060"
data_git_msg = """\
commit 37674c060e3658e035fab8901641344fb1a16741
Author: Weicai Yang <weicai@google.com>
Date:   Fri Feb 11 16:28:22 2022 -0800

    [dv] exclude d_user.rsp_intg[6] for xcelium
    
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
