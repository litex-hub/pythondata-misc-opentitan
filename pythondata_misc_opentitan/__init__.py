import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8918"
version_tuple = (0, 0, 8918)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8918")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8806"
data_version_tuple = (0, 0, 8806)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8806")
except ImportError:
    pass
data_git_hash = "d2c31411b881704bf640b7160e7973e700cb6b7b"
data_git_describe = "v0.0-8806-gd2c31411b"
data_git_msg = """\
commit d2c31411b881704bf640b7160e7973e700cb6b7b
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 29 18:41:03 2021 -0800

    [rv_core_ibex] Fix recov_alert behavior
    
    - Fixes #9415
    - Make software alerts mubi types and make recoverable error self clearing
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
