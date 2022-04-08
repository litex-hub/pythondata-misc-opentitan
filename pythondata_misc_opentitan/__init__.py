import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11458"
version_tuple = (0, 0, 11458)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11458")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11332"
data_version_tuple = (0, 0, 11332)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11332")
except ImportError:
    pass
data_git_hash = "32dd3e967535ba785e36f4a9b96ae447527127df"
data_git_describe = "v0.0-11332-g32dd3e967"
data_git_msg = """\
commit 32dd3e967535ba785e36f4a9b96ae447527127df
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 8 00:11:23 2022 +0100

    [tlul,lint] Tell verilator to split some signals in tlul_lc_gate.sv
    
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
