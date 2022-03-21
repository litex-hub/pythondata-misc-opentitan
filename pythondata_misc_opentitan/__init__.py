import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11002"
version_tuple = (0, 0, 11002)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11002")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10876"
data_version_tuple = (0, 0, 10876)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10876")
except ImportError:
    pass
data_git_hash = "d0aad7742f2837ca3b3fe37b92f6470c866c4139"
data_git_describe = "v0.0-10876-gd0aad7742"
data_git_msg = """\
commit d0aad7742f2837ca3b3fe37b92f6470c866c4139
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 2 14:00:33 2022 -0800

    [dv/unr] Blackbox common security modules from UNR flow
    
    This PR blackbox common security prim modules: prim_count,
    prim_double_lfsr, prim_sparse_fsm_flop from the UNR flow.
    
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
