import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10486"
version_tuple = (0, 0, 10486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10360"
data_version_tuple = (0, 0, 10360)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10360")
except ImportError:
    pass
data_git_hash = "1e16f2cc2c78182d93c3276731f67110223247d4"
data_git_describe = "v0.0-10360-g1e16f2cc2"
data_git_msg = """\
commit 1e16f2cc2c78182d93c3276731f67110223247d4
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Tue Feb 22 18:06:24 2022 +0000

    [sw,tests] Verify that the data within the retention SRAM survives low power entry-exit
    
    For test: chip_sw_sleep_sram_ret_contents.
    
    This test writes data to the retention SRAM and then enters low power mode. Upon wake
    from low power the data is read back and checked against the original data written.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
