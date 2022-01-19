import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9615"
version_tuple = (0, 0, 9615)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9615")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9493"
data_version_tuple = (0, 0, 9493)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9493")
except ImportError:
    pass
data_git_hash = "aa35abbf0683f2dcbf1e75451d4f5380164908f2"
data_git_describe = "v0.0-9493-gaa35abbf0"
data_git_msg = """\
commit aa35abbf0683f2dcbf1e75451d4f5380164908f2
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Thu Jan 6 13:22:09 2022 +0000

    [lc_ctrl/dv] Added test lc_ctrl_stress_all
    
    - Added test sequences:
      - lc_ctrl_stress_all_vseq.sv
     Randomly cycles through the other sequences and randomly choosing
     TL or JTAG for CSR access for that sequence
      - lc_ctrl_security_escalation_vseq.sv
     Randomly triggers an escalation while the process to transition is
     occuring so as to exercise all the <state> -> escalate arcs of the FSM
    - Fixed lc_ctrl_smoke_vseq which needed to set cfg.test_phase
    - Fixed lc_ctrl_errors_vseq so it can be rerun by lc_ctrl_stress_all
    - Fixed scoreboard for new escalate scenarios
    to avoid scoreboard errors when run after another sequence.
    - Added test_sequence_typename string to lc_ctrl_if to aid debugging
    this is set to to the test sequence typename at the start of each sequence.
    
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
