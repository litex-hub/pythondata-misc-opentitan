import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9344"
version_tuple = (0, 0, 9344)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9344")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9227"
data_version_tuple = (0, 0, 9227)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9227")
except ImportError:
    pass
data_git_hash = "5989d2abf4c3890f927579c9ba4b845cb6d553d0"
data_git_describe = "v0.0-9227-g5989d2abf"
data_git_msg = """\
commit 5989d2abf4c3890f927579c9ba4b845cb6d553d0
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Wed Dec 22 17:18:55 2021 +0000

    [lc_ctrl/dv] Implemented jtag_access jtag_priority and regwen_during_op testpoints
    
    - Added test sequences:
      - lc_ctrl_jtag_access_vseq to test the the mutex controlled registers via
      both the locked and unlocked interface to verify the interfaces and mutex
      control.
      - lc_ctrl_jtag_priority_vseq to test that when claiming the mutex that
      JTAG has priority over Tile Link
      - lc_ctrl_regwen_during_op_vseq to test mutex controlled registers are
      locked during state transition
    - Added tests:
      - lc_ctrl_jtag_access
      - lc_ctrl_jtag_smoke
      - lc_ctrl_jtag_state_post_trans
      - lc_ctrl_jtag_errors
      - lc_ctrl_jtag_prog_failure
      - lc_ctrl_jtag_csr_hw_reset
      - lc_ctrl_jtag_csr_rw
      - lc_ctrl_jtag_csr_bit_bash
      - lc_ctrl_jtag_csr_aliasing
      - lc_ctrl_jtag_same_csr_outstanding
      - lc_ctrl_jtag_csr_mem_rw_with_rand_reset
      - lc_ctrl_jtag_alert_test
      - lc_ctrl_regwen_during_op
      - lc_ctrl_jtag_regwen_during_op
    - Added regression jtag
    - Fixed up sequences for corrected status ready bit semantics
    from PR #9860
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
