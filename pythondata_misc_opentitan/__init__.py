import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10906"
version_tuple = (0, 0, 10906)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10906")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10780"
data_version_tuple = (0, 0, 10780)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10780")
except ImportError:
    pass
data_git_hash = "ccffc9806b894c0c6e865af12a5b8c71a1419ae3"
data_git_describe = "v0.0-10780-gccffc9806"
data_git_msg = """\
commit ccffc9806b894c0c6e865af12a5b8c71a1419ae3
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Mar 8 17:58:35 2022 -0800

    [dv/full_chip] Add clkmgr_external_clk_src_for_sw
    
    Fix chip external clock frequency: set it to 100 MHz by default, and add
    option to set it to either 100 or 48 MHz via "extclk_freq_mhz" plusargs.
    Create clkmgr_testutils_enable_clock_count_measurement testutils for
    this test.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
