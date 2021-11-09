import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8649"
version_tuple = (0, 0, 8649)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8649")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8537"
data_version_tuple = (0, 0, 8537)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8537")
except ImportError:
    pass
data_git_hash = "9f7d8ccc6ab98c080e62c79e191dbed759490920"
data_git_describe = "v0.0-8537-g9f7d8ccc6"
data_git_msg = """\
commit 9f7d8ccc6ab98c080e62c79e191dbed759490920
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Nov 5 23:17:56 2021 -0700

    [dv/pwrmgr] Enhance wakeup test
    
    Randomize enabling wake_info capture.
    Fix handling enables portion of `control` CSR.
    Fix control coverage.
    Enable the test in the testplan.
    
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
