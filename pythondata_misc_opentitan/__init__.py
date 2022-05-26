import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12360"
version_tuple = (0, 0, 12360)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12360")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12220"
data_version_tuple = (0, 0, 12220)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12220")
except ImportError:
    pass
data_git_hash = "402b325ecfdc8e6976baaacd798fac8763e74445"
data_git_describe = "v0.0-12220-g402b325ec"
data_git_msg = """\
commit 402b325ecfdc8e6976baaacd798fac8763e74445
Author: Alexander Williams <awill@google.com>
Date:   Tue May 24 09:19:46 2022 -0700

    [fpga] Bring AON clk down to 250 kHz
    
    Use the MMCM's cascaded dividers to bring the clock frequency down and
    align with the software's constants.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
