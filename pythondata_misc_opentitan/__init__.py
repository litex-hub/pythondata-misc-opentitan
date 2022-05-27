import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12389"
version_tuple = (0, 0, 12389)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12389")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12249"
data_version_tuple = (0, 0, 12249)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12249")
except ImportError:
    pass
data_git_hash = "a4c0586a87f2bd472c7346aedf9cff9e9dc39f28"
data_git_describe = "v0.0-12249-ga4c0586a8"
data_git_msg = """\
commit a4c0586a87f2bd472c7346aedf9cff9e9dc39f28
Author: Alexander Williams <awill@google.com>
Date:   Mon May 23 21:33:05 2022 -0700

    [usbdev] Quick fix to match example to FPGA pin-out
    
    The DIP switches seem to have swapped positions with LEDs.
    
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
