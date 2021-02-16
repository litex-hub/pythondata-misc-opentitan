import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5003"
version_tuple = (0, 0, 5003)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5003")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4912"
data_version_tuple = (0, 0, 4912)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4912")
except ImportError:
    pass
data_git_hash = "cf45be18d91183f9ee3555c83b446255bcbd92d6"
data_git_describe = "v0.0-4912-gcf45be18d"
data_git_msg = """\
commit cf45be18d91183f9ee3555c83b446255bcbd92d6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 15 08:37:11 2021 +0000

    [tlul] Update verilator waiver for tlul_err_resp
    
    Commit 041c683 fixed the d_size response from tlul_err_resp and, in
    doing so, read some more bits from tl_h_i. This commit updates the
    Verilator waiver so that it matches the warning message again.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
