import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10850"
version_tuple = (0, 0, 10850)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10850")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10724"
data_version_tuple = (0, 0, 10724)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10724")
except ImportError:
    pass
data_git_hash = "b40ec27bf69345d00908b352e08ef1c9d0a58e36"
data_git_describe = "v0.0-10724-gb40ec27bf"
data_git_msg = """\
commit b40ec27bf69345d00908b352e08ef1c9d0a58e36
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Fri Mar 11 13:08:47 2022 +0000

    [adc_ctrl/dv] Added reset tests
    
    - Added tests
      - adc_ctrl_fsm_reset
    - Added sequences
      - adc_ctrl_fsm_reset_vseq - randomly assert software/hardware reset for
      all ADC_CTRL modes preloading counters to minimise simulation time.
    - Added assertions in adc_ctrl_fsm_sva
      - FsmStateSwReset_A check FSM software reset
      - PwrupTimerCntSwReset_A check power up counter software reset
      - WakeupTimerCntSwReset_A check wake up counter software reset
      - NpSampleCntSwReset_A check normal power sample counter software reset
      - LpSampleCntSwReset_A check low power sample counter software reset
      - FsmStateHwReset_A check FSM hardware reset
      - PwrupTimerCntHwReset_A check power up counter hardware reset
      - WakeupTimerCntHwReset_A check wake up counter hardware reset
      - NpSampleCntHwReset_A check normal power sample counter hardware reset
      - LpSampleCntHwReset_A check low power sample counter hardware reset
    - Fixed wake up assertion auxiliary code.
    - Renamed enumeration constants to fit coding guidelines
    - Fixed EnterLowPower_A to be disabled when not in low power test mode.
    - Added hook task post_adc_ctrl_enable to adc_ctrl_filters_polled_vseq.sv
    - Killing background tasks in adc_ctrl_filters_polled_vseq::post_start
    
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
