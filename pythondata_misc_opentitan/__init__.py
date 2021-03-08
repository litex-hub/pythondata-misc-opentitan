import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5289"
version_tuple = (0, 0, 5289)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5289")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5194"
data_version_tuple = (0, 0, 5194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5194")
except ImportError:
    pass
data_git_hash = "1715552d57f007905965062c21d2a0f2e77db554"
data_git_describe = "v0.0-5194-g1715552d5"
data_git_msg = """\
commit 1715552d57f007905965062c21d2a0f2e77db554
Author: Weicai Yang <weicai@google.com>
Date:   Mon Mar 8 13:00:01 2021 -0800

    [aon_timer] Remove temporary intr_enable for #5260
    
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
