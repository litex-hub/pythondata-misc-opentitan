import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11134"
version_tuple = (0, 0, 11134)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11134")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11008"
data_version_tuple = (0, 0, 11008)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11008")
except ImportError:
    pass
data_git_hash = "b53c3b8433edcc52e2f1b45a6581e6bf447f5f0c"
data_git_describe = "v0.0-11008-gb53c3b843"
data_git_msg = """\
commit b53c3b8433edcc52e2f1b45a6581e6bf447f5f0c
Author: Weicai Yang <weicai@google.com>
Date:   Thu Mar 24 15:13:25 2022 -0700

    [dv] Fix clkmgr_cov_bind for lc_tx_t type ports
    
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
