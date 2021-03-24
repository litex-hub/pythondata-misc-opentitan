import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5565"
version_tuple = (0, 0, 5565)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5565")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5470"
data_version_tuple = (0, 0, 5470)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5470")
except ImportError:
    pass
data_git_hash = "4ca4a2f07bce8912d6adc10a56584319cea67491"
data_git_describe = "v0.0-5470-g4ca4a2f07"
data_git_msg = """\
commit 4ca4a2f07bce8912d6adc10a56584319cea67491
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 19 13:51:39 2021 -0700

    [sw] Prototype hardware memory init
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
