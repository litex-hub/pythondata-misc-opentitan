import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9329"
version_tuple = (0, 0, 9329)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9329")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9212"
data_version_tuple = (0, 0, 9212)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9212")
except ImportError:
    pass
data_git_hash = "616eadc1a1133ac45421f32ecc8d4458ca1daf4c"
data_git_describe = "v0.0-9212-g616eadc1a"
data_git_msg = """\
commit 616eadc1a1133ac45421f32ecc8d4458ca1daf4c
Author: Weicai Yang <weicai@google.com>
Date:   Thu Dec 30 15:28:51 2021 -0800

    [sram/dv] Enable stress test
    
    Also fix some failures in stress_all and stress_all with reset
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
