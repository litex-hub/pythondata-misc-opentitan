import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8832"
version_tuple = (0, 0, 8832)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8832")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8720"
data_version_tuple = (0, 0, 8720)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8720")
except ImportError:
    pass
data_git_hash = "fbccf8ef6d0c53bca5701e59eb6b5d3283393180"
data_git_describe = "v0.0-8720-gfbccf8ef6"
data_git_msg = """\
commit fbccf8ef6d0c53bca5701e59eb6b5d3283393180
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Nov 19 00:33:59 2021 +0000

    [spi_device] Connect SPI Flash Upload interrupts
    
    This commit connects the interrupts in SPI Device Flash mode.
    
    - cmdfifo_not_empty: Event occurs when SPI Flash device receives a
      command byte and the matched command information entry's upload bit is
      set.
    - payload_not_empty: If the received command has payload field, the
      upload module stores the incoming payload into DPSRAM Payload buffer.
      It then updates the payload size when SPI transaction is completed.
      The logic reports this event when the payload size is non-zero.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
