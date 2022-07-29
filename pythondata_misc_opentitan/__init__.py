import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13333"
version_tuple = (0, 0, 13333)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13333")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13191"
data_version_tuple = (0, 0, 13191)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13191")
except ImportError:
    pass
data_git_hash = "d95d53edde0b78ac811ebbaea8d5993a61f6ae93"
data_git_describe = "v0.0-13191-gd95d53edde"
data_git_msg = """\
commit d95d53edde0b78ac811ebbaea8d5993a61f6ae93
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jul 28 15:08:18 2022 -0700

    fix(kmac): Use `mode_q` to request EDN
    
    Issue https://github.com/lowRISC/opentitan/issues/13872
    
    Problem
    -------
    
    KMAC Entropy module reports Unknown Assertion error if SW changes the
    entropy mode from SW to Edn while operating.
    
    Analysis
    --------
    
    The entropy module latches the entropy mode when SW configures the
    `entropy_ready` bit. The mode is to select the LFSRs' seed input data
    between EDN data and SW seed CSR.
    
    Somehow, the module reseeds LFSRs from EDN if SW changes the mode while
    active. The state machine moves to `StRandEdn` state. The FSM sees
    `mode_i` in `StRandReady` rather than the latched version `mode_q`.
    
    Resolution
    ----------
    
    Changed the logic to look at `mode_q`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
