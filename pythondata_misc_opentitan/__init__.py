import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10928"
version_tuple = (0, 0, 10928)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10928")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10802"
data_version_tuple = (0, 0, 10802)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10802")
except ImportError:
    pass
data_git_hash = "2a2eb5ff7d8db22445086f6cf60cda29b59308b5"
data_git_describe = "v0.0-10802-g2a2eb5ff7"
data_git_msg = """\
commit 2a2eb5ff7d8db22445086f6cf60cda29b59308b5
Author: TIM EWINS <tim.ewins@ensilica.com>
Date:   Fri Mar 4 11:10:10 2022 +0000

    [flash_ctrl] ADD TEST FOR THE HOST CTRL ARBITER
    
    Perform operations via the Flash Software Interface, and at the same time invoke a
    Hardware RMA operation. This verifies the arbitration within the Flash Protocol
    Controller. The arbiter should allow any outstanding Software operations to complete
    before the RMA starts.  When the RMA completes the RMA FSM remains in its final state
    until Reset and Software access is blocked.
    
    Signed-off-by: TIM EWINS <tim.ewins@ensilica.com>

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
