import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9846"
version_tuple = (0, 0, 9846)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9846")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9722"
data_version_tuple = (0, 0, 9722)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9722")
except ImportError:
    pass
data_git_hash = "a1ba95ee32a5e77992da21b0d8230af8e5f7112f"
data_git_describe = "v0.0-9722-ga1ba95ee3"
data_git_msg = """\
commit a1ba95ee32a5e77992da21b0d8230af8e5f7112f
Author: Alexander Williams <awill@google.com>
Date:   Thu Jan 20 19:24:36 2022 -0800

    [usbdev] Move sense to an MIO
    
    The ASIC was missing a connection for the VBUS detection, so the MIO
    adds that. In addition, the FPGAs connect the two VBUS detection sources
    to IOR0 and IOR1--Software will have to select the correct I/O based on
    the `use_uphy` value.
    
    Moving to an MIO brings straightforward options for a simple constant
    via periph_insel if OT is completely bus-powered, in addition to
    making it available to both power domains for usbdev.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
