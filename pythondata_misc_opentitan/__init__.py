import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5126"
version_tuple = (0, 0, 5126)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5126")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5035"
data_version_tuple = (0, 0, 5035)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5035")
except ImportError:
    pass
data_git_hash = "51651f83e1795d99d86eb222829714b1c7567198"
data_git_describe = "v0.0-5035-g51651f83e"
data_git_msg = """\
commit 51651f83e1795d99d86eb222829714b1c7567198
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Feb 22 18:45:26 2021 -0800

    [dv/otp_ctrl] enable checking for interrupts and collect coverage
    
    This PR is related to interrupts:
    1. Support checking for interrupt related registers (except intr_state
    waiting for designer's confirmation)
    2. Ignored checking for status field `dai_idle` during dai operation,
    because scb does not accurately predict which cycle dai operation
    finishes.
    Also move status prediction to addr_read_phase instead of
    data_read_phase.
    3. Change status `enum` from value to index because it is easier to use
    index in scb.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
