import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12487"
version_tuple = (0, 0, 12487)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12487")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12345"
data_version_tuple = (0, 0, 12345)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12345")
except ImportError:
    pass
data_git_hash = "3114d148c0385c6c254b169a435cf03744f64549"
data_git_describe = "v0.0-12345-g3114d148c"
data_git_msg = """\
commit 3114d148c0385c6c254b169a435cf03744f64549
Author: Abdullah Varici <abdullah.varici@lowrisc.org>
Date:   Thu May 26 16:46:10 2022 +0100

    [sca] Add support for AES TVLA fixed-vs-random key captures in batch mode.
    
    In order to simplify the analysis, the first encryption has to use
    fixed key. In addition a PRNG is used for random key and plaintext
    generation instead of AES algorithm as specified in the TVLA DTR.
    
    Signed-off-by: Abdullah Varici <abdullah.varici@lowrisc.org>

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
