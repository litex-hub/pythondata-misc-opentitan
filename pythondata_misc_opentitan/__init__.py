import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11364"
version_tuple = (0, 0, 11364)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11364")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11238"
data_version_tuple = (0, 0, 11238)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11238")
except ImportError:
    pass
data_git_hash = "faab4c52b820fc5121890174e512c23b61b9a722"
data_git_describe = "v0.0-11238-gfaab4c52b"
data_git_msg = """\
commit faab4c52b820fc5121890174e512c23b61b9a722
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Apr 4 15:22:34 2022 -0700

    [dv/otp_ctrl] Improve FSM coverage
    
    This PR improves the FSM cov with the following updates:
    1). Add support in smoke test to issue reset during pwr_init.
        This targets to hit FSM cov from init states to reset states.
    2). Move `apply_resets_concurrently` override to common_vseq because it
        only common tests need this override.
    3). Remove the constraints about ECC correctable errors and timeout
        error. I believe scb can handle both cases.
    4). Remove the pre-conditions to write ral.check_timeout register.
    
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
