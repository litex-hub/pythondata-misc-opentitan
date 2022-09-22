import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14387"
version_tuple = (0, 0, 14387)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14387")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14245"
data_version_tuple = (0, 0, 14245)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14245")
except ImportError:
    pass
data_git_hash = "8bf8012ef4548b7b783ee50a7b81c37107c8f18d"
data_git_describe = "v0.0-14245-g8bf8012ef4"
data_git_msg = """\
commit 8bf8012ef4548b7b783ee50a7b81c37107c8f18d
Author: Drew Macrae <drewmacrae@google.com>
Date:   Fri Sep 16 10:46:50 2022 -0400

    [i2c dif] Add headers for functions to control i2c device in the dif
    
    * Changed documentation references to consistently refer to FMT and RX
      buffers as FIFOs when applying names and short descriptions
    * Added a documentation referring to ability to reset the I2C block
      (because it might be useful)
    * Changed documentation references to RESTART to repeated START to
      make them more consistent with I2C standards
    * Annotated states with Shared, host and device mode to help track
      which features acted in which modes
    * Updated header for i2c_dif to support device mode and clarify
      which registers control which modes
    * corrected FIFO references in device tx rx test portion of
      testplan and added requirement to perform an I2C read
    * fixed i2c_dif_unittest that swapped rx and fmt fifo levels
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
