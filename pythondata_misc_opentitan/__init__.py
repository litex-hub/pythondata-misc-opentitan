import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8200"
version_tuple = (0, 0, 8200)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8200")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8088"
data_version_tuple = (0, 0, 8088)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8088")
except ImportError:
    pass
data_git_hash = "901edd1099bcf1583e504a5e60103363854b6ba7"
data_git_describe = "v0.0-8088-g901edd109"
data_git_msg = """\
commit 901edd1099bcf1583e504a5e60103363854b6ba7
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Oct 8 12:19:25 2021 -0700

    [dv/pwrmgr] Consolidate reset tests
    
    Merge conditional and unconditional escalation and main power glitch
    reset tests.
    Also fixes trivial formattter issues.
    
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
