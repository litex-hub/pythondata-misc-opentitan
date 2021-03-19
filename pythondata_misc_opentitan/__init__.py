import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5484"
version_tuple = (0, 0, 5484)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5484")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5389"
data_version_tuple = (0, 0, 5389)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5389")
except ImportError:
    pass
data_git_hash = "0e1e8aad9e3065fa7cb8354d211fe6e0a6fdc419"
data_git_describe = "v0.0-5389-g0e1e8aad9"
data_git_msg = """\
commit 0e1e8aad9e3065fa7cb8354d211fe6e0a6fdc419
Author: Hoang Tung <Hoang.Tung@wdc.com>
Date:   Sun Mar 14 23:41:18 2021 -0700

    [pwm, dv] Add WiP DV for PWM, all *csr tests pass
    
      - add pwm_agent (device mode) with empty driver
        (pwm does not require response from agent)
      - add env dv supports *csr tests
      - add tb.sv with 2 dependent clock and reset sources (core_clk_freq <= bus_clk_freq)
      - add pwm_testplan.hjson to the list in build_docs.py script
    
    Signed-off-by: Hoang Tung <Hoang.Tung@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
