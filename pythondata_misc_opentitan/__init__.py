import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14896"
version_tuple = (0, 0, 14896)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14896")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14754"
data_version_tuple = (0, 0, 14754)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14754")
except ImportError:
    pass
data_git_hash = "48bfeae1f027a5d78808043b3165e268176b82af"
data_git_describe = "v0.0-14754-g48bfeae1f0"
data_git_msg = """\
commit 48bfeae1f027a5d78808043b3165e268176b82af
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Oct 21 15:26:35 2022 -0700

    [fpv/rstmgr] Configure additional clocks for fpv
    
    The rstmgr unit uses multiple clocks, which fpv assertions use.
    The default fpv settings only configure clk_i, so many fpv
    assertions had no chance of working.
    
    This change assumes CDC is correct, so it simplifies the clock frequency
    and phase relations.
    
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
