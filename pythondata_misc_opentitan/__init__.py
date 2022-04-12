import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11530"
version_tuple = (0, 0, 11530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11404"
data_version_tuple = (0, 0, 11404)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11404")
except ImportError:
    pass
data_git_hash = "48a3d40d2122cf3f3783314028add56b8f39fd30"
data_git_describe = "v0.0-11404-g48a3d40d2"
data_git_msg = """\
commit 48a3d40d2122cf3f3783314028add56b8f39fd30
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Thu Mar 31 17:39:55 2022 +0100

    [sw,tests] Enter RMA LC_STATE and check flash access and wipe
    
    For tests:
    chip_sw_flash_rma_unlocked
    chip_sw_flash_creator_seed_wipe_on_rma
    
    The system is initially started in Dev LC_STATE and data is written to all flash partitions.
    The system is then set to enter RMA mode. After entry the flash is read again and checked
    that the flash is accessible and that the contents have been wiped and differ from the
    previously written values.
    
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
