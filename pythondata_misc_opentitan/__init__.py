import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5569"
version_tuple = (0, 0, 5569)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5569")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5474"
data_version_tuple = (0, 0, 5474)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5474")
except ImportError:
    pass
data_git_hash = "5f1d304ad5c63a428219d1881479707727a559de"
data_git_describe = "v0.0-5474-g5f1d304ad"
data_git_msg = """\
commit 5f1d304ad5c63a428219d1881479707727a559de
Author: Eric Shiu <eshiu@google.com>
Date:   Wed Mar 17 17:24:11 2021 -0700

    [adc_ctrl] rename dcd to adc_ctrl
    
    Signed-off-by: Eric Shiu <eshiu@google.com>

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
