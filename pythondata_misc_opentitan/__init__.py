import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10932"
version_tuple = (0, 0, 10932)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10932")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10806"
data_version_tuple = (0, 0, 10806)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10806")
except ImportError:
    pass
data_git_hash = "aa9daa1b8696412230a6d81bd1651fd8ae672d12"
data_git_describe = "v0.0-10806-gaa9daa1b8"
data_git_msg = """\
commit aa9daa1b8696412230a6d81bd1651fd8ae672d12
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Mar 15 18:15:58 2022 -0700

    [rtl/otp] Some workaround for FPV security countermeasure assertions
    
    Hi Michael,
    I do not think they are necessary RTL functional changes, but related to
    how formal checks these security countermeasure assertions.
    What we did are:
    - blackbox prim_counts and prim_lfsrs
    - stop at the logic with sparse_fsm outputs
    The side-effects of these manual injections are - at some cases,
    `state_q <= state_d` does not work anymore.
    
    So if the prim_counter has err_o, sometimes it only propogates to
    state_d but not state_q. So it will never trigger a `fsm_err_o`. Please
    see the waves attached.
    
    Because of that, I think maybe this workaround would work?
    If you do not want it to be in the acutal RTL code, I can also add a
    ifdef `FPV_SEC_CM_ON` to only include these code in FPV.
    Please let me know what you think.
    
    Thanks
    Cindy
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
