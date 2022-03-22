import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11026"
version_tuple = (0, 0, 11026)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11026")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10900"
data_version_tuple = (0, 0, 10900)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10900")
except ImportError:
    pass
data_git_hash = "110bf9869abd71c82a894790a62ec8956dda7b14"
data_git_describe = "v0.0-10900-g110bf9869"
data_git_msg = """\
commit 110bf9869abd71c82a894790a62ec8956dda7b14
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Tue Mar 22 18:11:17 2022 +0000

    [adc_ctrl/dv] Added adc_ctrl_stress_all test
    
    - Added tests
      - adc_ctrl_stress_all
    - Added test sequences
      - adc_ctrl_stress_all_vseq - runs a random choice of the others test sequences
    - Fixed adc_ctrl_intr - Disabled scoreboard and enabled autopredict
    - Fixed adc_ctrl_bit_bash - Added assertion control ADC_CTRL_FSM_A_CTRL
    - Fixed adc_ctrl_clock_gating - Disabled interrupts for this test
    - Corrected filter parameter coverage
    - Enhanced variable filter config constraints to generate maximum and
    minimum values for min_v and max_v
    - Added reads of channel value registers to interrupt/both tests
    - Aligned capture of interrupt channel values in model with RTL
    - Modelling intr_test in scoreboard
    - Added interrupt cover groups sampling to scoreboard
    
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
