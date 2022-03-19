import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10996"
version_tuple = (0, 0, 10996)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10996")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10870"
data_version_tuple = (0, 0, 10870)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10870")
except ImportError:
    pass
data_git_hash = "4a8e83046253a916d9ed11ec132588d5bf2d9d95"
data_git_describe = "v0.0-10870-g4a8e83046"
data_git_msg = """\
commit 4a8e83046253a916d9ed11ec132588d5bf2d9d95
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Mar 17 00:33:36 2022 -0700

    [dif/adc_ctrl] Update DIF checklist
    
    This updates the DIF checklist for the ADC Controller to match the
    current state of the SW (all DIFs implemented).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
