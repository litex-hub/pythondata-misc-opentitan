import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11473"
version_tuple = (0, 0, 11473)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11473")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11347"
data_version_tuple = (0, 0, 11347)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11347")
except ImportError:
    pass
data_git_hash = "bb069b45a1d859edd14aacd0ae2dc6a028fba224"
data_git_describe = "v0.0-11347-gbb069b45a"
data_git_msg = """\
commit bb069b45a1d859edd14aacd0ae2dc6a028fba224
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 8 08:20:19 2022 +0100

    [keymgr,lint] Make some implicit widenings explicit
    
    This silences lint warnings from Verilator
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
