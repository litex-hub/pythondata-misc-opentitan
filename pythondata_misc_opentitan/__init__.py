import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13138"
version_tuple = (0, 0, 13138)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13138")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12996"
data_version_tuple = (0, 0, 12996)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12996")
except ImportError:
    pass
data_git_hash = "b802eaad8b300a1df13952ab77f328a13a025bc3"
data_git_describe = "v0.0-12996-gb802eaad8b"
data_git_msg = """\
commit b802eaad8b300a1df13952ab77f328a13a025bc3
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 30 17:40:47 2022 -0700

    [dv,chip,clkmgr] Add clkmgr_sleep_frequency test
    
    This test is marked as broken for cw310 and verilator because ast_init
    is not done, which defeats the clock measurements.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
