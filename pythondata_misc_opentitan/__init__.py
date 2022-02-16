import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10331"
version_tuple = (0, 0, 10331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10205"
data_version_tuple = (0, 0, 10205)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10205")
except ImportError:
    pass
data_git_hash = "b8e70c002ff2f34de0cb321db9c459f2e1908d45"
data_git_describe = "v0.0-10205-gb8e70c002"
data_git_msg = """\
commit b8e70c002ff2f34de0cb321db9c459f2e1908d45
Author: Weicai Yang <weicai@google.com>
Date:   Tue Feb 15 16:08:43 2022 -0800

    [dv] Add macro DV_LC_TX_DIST and update get_rand_lc_tx_val
    
    lc_tx_pkg::On/Off is different than Mubi4True/False
    Add a macro so that users can use `DV_LC_TX_DIST` in constraint
    And update `get_rand_lc_tx_val` to use this constraint macro
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
