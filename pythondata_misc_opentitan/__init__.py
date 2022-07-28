import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13308"
version_tuple = (0, 0, 13308)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13308")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13166"
data_version_tuple = (0, 0, 13166)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13166")
except ImportError:
    pass
data_git_hash = "ae9a6baef1c1e73cc4c73ce33b8cf5ad8e40a26d"
data_git_describe = "v0.0-13166-gae9a6baef1"
data_git_msg = """\
commit ae9a6baef1c1e73cc4c73ce33b8cf5ad8e40a26d
Author: Alexander Williams <awill@google.com>
Date:   Thu Jul 21 17:49:43 2022 -0700

    [cw310] Connect all pads
    
    This adds all the pads that were previously removed, including PMOD
    connections for a UART, I2C, and PWM.
    
    The LEDs and DIP switches have been moved, and the common pinmux
    function no longer automatically configures GPIOs. Adjust tests that use
    the GPIOs to set up their own pinmux config and map them to IOA2-IOA8
    only.
    
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
