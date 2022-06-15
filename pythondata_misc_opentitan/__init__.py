import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12700"
version_tuple = (0, 0, 12700)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12700")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12558"
data_version_tuple = (0, 0, 12558)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12558")
except ImportError:
    pass
data_git_hash = "7b78a79290e3475424ccc4f668edf3da9a97f2dd"
data_git_describe = "v0.0-12558-g7b78a7929"
data_git_msg = """\
commit 7b78a79290e3475424ccc4f668edf3da9a97f2dd
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Jun 6 20:51:40 2022 -0700

    [dv,chip_sw] Harden external_clk_src_for_lc test
    
    Detect when the external clock is selected to drive the ast io_clk output.
    
    Fixes: #12232
    
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
