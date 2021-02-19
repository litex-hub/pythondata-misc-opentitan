import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5056"
version_tuple = (0, 0, 5056)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5056")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4965"
data_version_tuple = (0, 0, 4965)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4965")
except ImportError:
    pass
data_git_hash = "f83947635f4426de2117f6aa433065806eed9ca8"
data_git_describe = "v0.0-4965-gf83947635"
data_git_msg = """\
commit f83947635f4426de2117f6aa433065806eed9ca8
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Feb 19 11:32:39 2021 +0100

    [csrng] Select Canright S-Box implementation for AES cipher core
    
    This commit changes the default selection for the S-Box implementation
    inside the embedded AES cipher core from the LUT-based implementation the
    unmasked Canright design. This is more suitable for ASIC implementations
    because of the lower area footprint. The LUT-based implementation should
    be used for FPGA targets only.
    
    This change got already merged with lowRISC/OpenTitan#5215 but it got
    accidentally reverted when rebasing lowRISC/OpenTitan#5195.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
