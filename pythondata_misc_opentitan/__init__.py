import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5428"
version_tuple = (0, 0, 5428)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5428")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5333"
data_version_tuple = (0, 0, 5333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5333")
except ImportError:
    pass
data_git_hash = "bfc5bf80a7eaebc8a0a89922f396088dc020f36b"
data_git_describe = "v0.0-5333-gbfc5bf80a"
data_git_msg = """\
commit bfc5bf80a7eaebc8a0a89922f396088dc020f36b
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Tue Mar 16 13:01:06 2021 -0700

    [edn/dv] V0->V1
    
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
