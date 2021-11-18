import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8763"
version_tuple = (0, 0, 8763)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8763")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8651"
data_version_tuple = (0, 0, 8651)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8651")
except ImportError:
    pass
data_git_hash = "0949f76ef5fea1045b8a25326f9d771004829ee8"
data_git_describe = "v0.0-8651-g0949f76ef"
data_git_msg = """\
commit 0949f76ef5fea1045b8a25326f9d771004829ee8
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Nov 17 09:44:32 2021 -0800

    [dv/rstmgr] Add sw_rst test to the testplan
    
    This test was developed some time ago but was not registered with the
    testplan.
    This also fixes randomization of rstmgr_por_stretcher test.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
