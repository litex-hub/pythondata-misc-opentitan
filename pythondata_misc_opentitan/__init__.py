import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8921"
version_tuple = (0, 0, 8921)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8921")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8809"
data_version_tuple = (0, 0, 8809)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8809")
except ImportError:
    pass
data_git_hash = "a81a99c5491f11e4ba06958b45ce246f0b0687b4"
data_git_describe = "v0.0-8809-ga81a99c54"
data_git_msg = """\
commit a81a99c5491f11e4ba06958b45ce246f0b0687b4
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 22 16:57:11 2021 -0800

    [adc_ctrl] Make handshake more robust
    
    - Fixes #9312
    - Ensure valid is dropped before moving to ensure we don't accidentally
      sample the same value multiple times.
    
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
