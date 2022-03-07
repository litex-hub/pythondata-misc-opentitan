import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10743"
version_tuple = (0, 0, 10743)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10743")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10617"
data_version_tuple = (0, 0, 10617)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10617")
except ImportError:
    pass
data_git_hash = "03ee2dcb4c0c1296421ecdb9fbeddf071a67141f"
data_git_describe = "v0.0-10617-g03ee2dcb4"
data_git_msg = """\
commit 03ee2dcb4c0c1296421ecdb9fbeddf071a67141f
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Mon Mar 7 13:28:07 2022 +0000

    [adc_ctrl/dv] Added counter tests
    
    - Added tests
      - adc_ctrl_poweron_counter
      - adc_ctrl_lowpower_counter
    - Added test sequences
      - adc_ctrl_counter_vseq
        Randomize wakeup_time powerup_time and low/high/one shot power mode, wait for data then repeat.
      - adc_ctrl_poweron_counter_vseq
        Extends adc_ctrl_counter_vseq for normal and one shot mode.
      - adc_ctrl_lowpower_counter_vseq
        Extends adc_ctrl_counter_vseq for low power mode.
    - Added assertions
      - WakeupTime_A - checks wakeup timing in low power mode
      - EnterLowPower_A - Checks ADC controller enters low power mode
    - Updated model
      - Updated to latest spec / RTL
      - Modelled adc_fsm_reset register
      - Modelled interrupt registers for One Shot mode.
    - Updated adc_ctrl_filters_polled_vseq to perform FSM reset at the end of each iteration as
    to make sure model and RTL are synchronised before each new configuration
    - Updated PwrupTime_A to new spec (programmed value + 1) cycles
    - Enabled PwrupTime_A for all tests and removed plusarg control
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

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
