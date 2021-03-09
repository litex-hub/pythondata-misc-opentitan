import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5311"
version_tuple = (0, 0, 5311)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5311")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5216"
data_version_tuple = (0, 0, 5216)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5216")
except ImportError:
    pass
data_git_hash = "67a5d9fc276d74bfbb8af035560a01ade5ae5604"
data_git_describe = "v0.0-5216-g67a5d9fc2"
data_git_msg = """\
commit 67a5d9fc276d74bfbb8af035560a01ade5ae5604
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Thu Feb 25 07:19:46 2021 -0800

    [edn/dv] csrng_agent device mode, edn_smoke_test
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
