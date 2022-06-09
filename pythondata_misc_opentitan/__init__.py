import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12622"
version_tuple = (0, 0, 12622)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12622")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12480"
data_version_tuple = (0, 0, 12480)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12480")
except ImportError:
    pass
data_git_hash = "24d368c57633e0e9ee2e0f3f400988e7a3ab4629"
data_git_describe = "v0.0-12480-g24d368c57"
data_git_msg = """\
commit 24d368c57633e0e9ee2e0f3f400988e7a3ab4629
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Mon May 30 18:20:58 2022 +0100

    [sw,tests] Update SRAM scramble tests to handle ECC errors
    
    For tests:
    chip_sw_sram_ctrl_main_scrambled_access
    chip_sw_sram_ctrl_main_scrambled_access_jitter_en
    chip_sw_sram_ctrl_ret_scrambled_access
    
    The tests have been updated to handle ECC errors in the readback data. Previously,
    this was not needed as ECC checking was not enabled. It was sufficient to write
    data, scramble, read back and check for mismatches against the original data. ECC errors
    now trigger an internal interrupt in the CPU. An exception handler has been written for
    this. In addition to the read back check, a count of the number of exceptions handled
    is kept and checked against the expected number.
    
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
