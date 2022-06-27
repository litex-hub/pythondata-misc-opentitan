import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12857"
version_tuple = (0, 0, 12857)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12857")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12715"
data_version_tuple = (0, 0, 12715)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12715")
except ImportError:
    pass
data_git_hash = "45c1e420d635c0eb28557f02f3dd04f4ab028656"
data_git_describe = "v0.0-12715-g45c1e420d6"
data_git_msg = """\
commit 45c1e420d635c0eb28557f02f3dd04f4ab028656
Author: Alexander Williams <awill@google.com>
Date:   Thu Jun 23 10:20:01 2022 -0700

    [usbdev] Remove internal CDC logic
    
    With the CSR clock now required to be the 48 MHz USB clock, there is no
    domain crossing between the TL-UL side and the internals (within the
    module). Instead, the clock domain crossing is outside the module (in
    xbar_main, in this case).
    
    Also change AV FIFO empty / RX FIFO full interrupts to reflect the
    status, instead of waiting for an underflow / overflow event.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
