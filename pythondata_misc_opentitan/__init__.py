import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12838"
version_tuple = (0, 0, 12838)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12838")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12696"
data_version_tuple = (0, 0, 12696)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12696")
except ImportError:
    pass
data_git_hash = "c1328144a07ccd2120eb7b3159a636c4b16f27bd"
data_git_describe = "v0.0-12696-gc1328144a0"
data_git_msg = """\
commit c1328144a07ccd2120eb7b3159a636c4b16f27bd
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Wed Jun 15 10:57:33 2022 +0100

    [sw,tests] Verify sysrst_ctrl inputs can be read using CSRs
    
    For test:
    chip_sw_sysrst_ctrl_inputs
    
    Checks that known values driven at the chip inputs by the testbench
    can be read using the sysrst_ctrl CSRs in software. The values read
    are verified against the expected values.
    
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
