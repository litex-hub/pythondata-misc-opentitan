import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9635"
version_tuple = (0, 0, 9635)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9635")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9513"
data_version_tuple = (0, 0, 9513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9513")
except ImportError:
    pass
data_git_hash = "40c007a05bf96e2413887650bf110c12196322e3"
data_git_describe = "v0.0-9513-g40c007a05"
data_git_msg = """\
commit 40c007a05bf96e2413887650bf110c12196322e3
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Tue Oct 19 15:46:28 2021 +0100

    [adc_ctrl/dv] Added ADC push pull agents and smoke test
    
    - Added test sequence adc_ctrl_smoke_vseq.sv
    Configures DUT in one-shot mode and ensures ADC data is stored in
    the sample registers.
    - Integrated push pull agents into environment to emulate the
    AST ADC
    - Added filter configuration fields to config object and configuration
    task in preparation for other tests.
    - Added filters_both testpoint to testplan
    - Added a short delay at the end of adc_ctrl_common_vseq body to
    allow register CDC to finish and avoid triggering assertions at the
    end of the test.
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
