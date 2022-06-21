import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12760"
version_tuple = (0, 0, 12760)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12760")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12618"
data_version_tuple = (0, 0, 12618)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12618")
except ImportError:
    pass
data_git_hash = "7c8a371fadb1ec856842406c11d49892138b1518"
data_git_describe = "v0.0-12618-g7c8a371fad"
data_git_msg = """\
commit 7c8a371fadb1ec856842406c11d49892138b1518
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jun 16 22:47:05 2022 -0700

    [sram, dv] Update intg_test_err
    
    Aligned with design that detecting fault injection gates all mem access.
    The access after FI won't be blocked but it causes a fatal alert
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
