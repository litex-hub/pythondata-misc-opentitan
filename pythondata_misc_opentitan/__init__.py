import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5818"
version_tuple = (0, 0, 5818)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5818")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5723"
data_version_tuple = (0, 0, 5723)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5723")
except ImportError:
    pass
data_git_hash = "1def47b2507b73b66d045695c03946e5349f738d"
data_git_describe = "v0.0-5723-g1def47b25"
data_git_msg = """\
commit 1def47b2507b73b66d045695c03946e5349f738d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 9 10:07:55 2021 +0100

    [keymgr] Define an intermediate signal for setting cfg_regwen
    
    This avoids an UNOPTFLAT warning from Verilator, caused because
    Verilator doesn't automatically split the hw2reg structure when
    topologically sorting the processes that read to and write from it.
    Another way to address this is to use a "split_var" Verilator-specific
    hint, but I think the code is also probably clearer for humans when
    rewritten this way.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
