import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10866"
version_tuple = (0, 0, 10866)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10866")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10740"
data_version_tuple = (0, 0, 10740)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10740")
except ImportError:
    pass
data_git_hash = "b72a638b010b936a2ba79024ce25d8e629a3bec6"
data_git_describe = "v0.0-10740-gb72a638b0"
data_git_msg = """\
commit b72a638b010b936a2ba79024ce25d8e629a3bec6
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Tue Mar 8 15:15:49 2022 +0000

    [sw,tests] Verify flash_idle signaling to pwrmgr
    
    For test: chip_sw_flash_idle_low_power.
    
    Checks that when low power entry is enabled and a flash operation is in progress that the
    low power entry is cancelled upon receiving the WFI instruction.
    The watchdog timer barks to exit the WFI and a check is done to ensure the flash operation has completed.
    
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
