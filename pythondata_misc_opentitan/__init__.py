import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5100"
version_tuple = (0, 0, 5100)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5100")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5009"
data_version_tuple = (0, 0, 5009)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5009")
except ImportError:
    pass
data_git_hash = "6a0baac71378994feca7154c19dac66b0aef3998"
data_git_describe = "v0.0-5009-g6a0baac71"
data_git_msg = """\
commit 6a0baac71378994feca7154c19dac66b0aef3998
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Feb 19 12:36:12 2021 -0800

    [dvsim] lint fixes to FlowCfg
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
