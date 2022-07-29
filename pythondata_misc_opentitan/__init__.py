import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13331"
version_tuple = (0, 0, 13331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13189"
data_version_tuple = (0, 0, 13189)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13189")
except ImportError:
    pass
data_git_hash = "d425d553f22422679d93f87551c3e49b6b920c1a"
data_git_describe = "v0.0-13189-gd425d553f2"
data_git_msg = """\
commit d425d553f22422679d93f87551c3e49b6b920c1a
Author: Nicholas Mosier <nmosier@google.com>
Date:   Tue Jul 26 20:33:31 2022 +0000

    [silicon_creator/spi_device] Fix fault injection bug in spi_device_cmd_get()
    
    We discovered a fault injection bug in spi_device_cmd_get() in
    sw/device/silicon_creator/lib/drivers/spi_device.c, in which the code
    copies the number of bytes given in a 9-bit byte count from the
    PAYLOAD_DEPTH field of the SPI device's STATUS2 register into an
    output buffer of size 256.  While the hardware ensures always that
    PAYLOAD_DEPTH <= 256, a fault injection causing a flip of one of the
    PAYLOAD_DEPTH bits causes a stack buffer overflow.
    
    We fixed this bug by (1) deriving the size of the
    spi_device_cmd_t::payload buffer from the size of the SPI device's
    payload buffer, and (2) performing a hardened bounds check on the
    PAYLOAD_DEPTH field read by the SPI device driver.
    
    Signed-off-by: Nicholas Mosier <nmosier@google.com>

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
