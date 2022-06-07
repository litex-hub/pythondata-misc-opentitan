import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12557"
version_tuple = (0, 0, 12557)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12557")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12415"
data_version_tuple = (0, 0, 12415)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12415")
except ImportError:
    pass
data_git_hash = "9808dea6681a618148bfacac22e26fcb6cdc05d9"
data_git_describe = "v0.0-12415-g9808dea66"
data_git_msg = """\
commit 9808dea6681a618148bfacac22e26fcb6cdc05d9
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Tue Jun 7 18:13:08 2022 +0100

    [sw,tests] Update timeout for retention SRAM contents test
    
    For test:
    chip_sw_sleep_sram_ret_contents
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
