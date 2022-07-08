import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13000"
version_tuple = (0, 0, 13000)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13000")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12858"
data_version_tuple = (0, 0, 12858)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12858")
except ImportError:
    pass
data_git_hash = "45121fcd36aa3e29e086e2a05acf70a564a8e635"
data_git_describe = "v0.0-12858-g45121fcd36"
data_git_msg = """\
commit 45121fcd36aa3e29e086e2a05acf70a564a8e635
Author: Alexander Williams <awill@google.com>
Date:   Wed Jun 29 16:37:48 2022 -0700

    [top] Separate JTAG from SPIDEV on CW310
    
    Align ASIC and CW310 JTAG pins on the pinmux. Move the VBUS sense pin
    for usbdev to IOC7, since IOR0 is used by JTAG.
    
    This commit connects CW310's JTAG header to the JTAG pins on IOR0-IOR4.
    Note that TRST_N is only available on the 20-pin header.
    
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
