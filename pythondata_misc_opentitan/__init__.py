import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14724"
version_tuple = (0, 0, 14724)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14724")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14582"
data_version_tuple = (0, 0, 14582)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14582")
except ImportError:
    pass
data_git_hash = "a34170ca0111f99e8bd1f742819710c3f9872156"
data_git_describe = "v0.0-14582-ga34170ca01"
data_git_msg = """\
commit a34170ca0111f99e8bd1f742819710c3f9872156
Author: Weicai Yang <weicai@google.com>
Date:   Tue Oct 11 22:02:29 2022 -0700

    [spi_device/dv] Test async fifo empty/full status
    
    Added in spi_device_intr to check async fifo empty/full status
    Also adjusted constraint for spi_device_fifo_full, so that it doesn't run more than 1hr
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
