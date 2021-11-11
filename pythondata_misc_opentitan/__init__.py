import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8675"
version_tuple = (0, 0, 8675)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8675")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8563"
data_version_tuple = (0, 0, 8563)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8563")
except ImportError:
    pass
data_git_hash = "69cb0a249e40399c89dabdd8c44db77612ec63f5"
data_git_describe = "v0.0-8563-g69cb0a249"
data_git_msg = """\
commit 69cb0a249e40399c89dabdd8c44db77612ec63f5
Author: Weicai Yang <weicai@google.com>
Date:   Wed Nov 10 00:08:44 2021 -0800

    [keymgr/dv] Fix shadow_reg_update_error_with_csr_rw
    
    Don't do operation in shadow_reg_errors_with_csr_rw, as the
    csr_rw_seq runs in parallel and issueing an operation affects CSR access.
    
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
