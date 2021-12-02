import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8961"
version_tuple = (0, 0, 8961)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8961")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8849"
data_version_tuple = (0, 0, 8849)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8849")
except ImportError:
    pass
data_git_hash = "974d70489a48b51fd3ac570044e32bbebad8f5be"
data_git_describe = "v0.0-8849-g974d70489"
data_git_msg = """\
commit 974d70489a48b51fd3ac570044e32bbebad8f5be
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sun Nov 7 15:15:26 2021 -0800

    [spi_host] Cleanup AscentLint errors, add waivers
    
    - Remove an ASSERT that was being flagged as a null assertion.
    - Request waivers for ascent lint rule CALC_NEXT_STATE for certain FSM state
      transitions, in which the SPI_HOST FSM uses signals to ensure that idle state
      transitions are performed consistently.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
