import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11276"
version_tuple = (0, 0, 11276)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11276")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11150"
data_version_tuple = (0, 0, 11150)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11150")
except ImportError:
    pass
data_git_hash = "a7dd5942185b02b928e3b03dc1c5ea38c4d7517a"
data_git_describe = "v0.0-11150-ga7dd59421"
data_git_msg = """\
commit a7dd5942185b02b928e3b03dc1c5ea38c4d7517a
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Thu Mar 31 19:47:57 2022 +0000

    [clkmgr,dv] fix regression failure
    
      - add back *_meas_ctrl_shadowed_* to exclusion list to avoid
        RECOV_ERR_CODE failure
      - update default idle value to false in csr test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
