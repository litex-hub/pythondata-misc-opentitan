import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11139"
version_tuple = (0, 0, 11139)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11139")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11013"
data_version_tuple = (0, 0, 11013)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11013")
except ImportError:
    pass
data_git_hash = "a609d5560844803b798391f76c5f87a11219f16c"
data_git_describe = "v0.0-11013-ga609d5560"
data_git_msg = """\
commit a609d5560844803b798391f76c5f87a11219f16c
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Fri Mar 25 17:18:46 2022 +0000

    [lc_ctrl/dv] Added common security countermeasures test.
    
    - Added sec_cm_tests.hjson to import list in lc_ctrl_sim_cfg.hjson
    - Imported sec_cm_pkg into lc_ctrl_env_pkg
    - Set sec_cm_alert_name to "fatal_state_error" in lc_ctrl_env_cfg
    - Checking status and lc_state registers in lc_ctrl_common_vseq
    - Checking DUT outputs in lc_ctrl_common_vseq
    - Added lc_ctrl_sec_cm, lc_ctrl_state_failure and lc_ctrl_tl_intg_err
      to lc_ctrl_sec_cm_testplan.hjson
    - Added MUBI coverage to lc_ctrl_cov_bind.sv
    
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
