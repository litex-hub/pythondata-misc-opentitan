import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11025"
version_tuple = (0, 0, 11025)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11025")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10899"
data_version_tuple = (0, 0, 10899)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10899")
except ImportError:
    pass
data_git_hash = "f95a6861273d99c46663532772a8a3b081e6efaf"
data_git_describe = "v0.0-10899-gf95a68612"
data_git_msg = """\
commit f95a6861273d99c46663532772a8a3b081e6efaf
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Mar 14 15:10:05 2022 -0700

    [spi_device] Revise spec to describe BUSY
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
