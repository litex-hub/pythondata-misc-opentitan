import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10493"
version_tuple = (0, 0, 10493)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10493")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10367"
data_version_tuple = (0, 0, 10367)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10367")
except ImportError:
    pass
data_git_hash = "fd1d80fd914472aa14f57ed80a7b24e20a723f7b"
data_git_describe = "v0.0-10367-gfd1d80fd9"
data_git_msg = """\
commit fd1d80fd914472aa14f57ed80a7b24e20a723f7b
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Feb 22 17:58:49 2022 -0800

    [fpv] V2S formal support
    
    This PR sets up the FPV environment to support V2S formal:
    1). Add a `task` enviornment input to indicate which subsets of
      assertions to run.
    2). Relax original `prim_assert_sec_cm.svh` alert timing because FPV
      might trigger other fatal alerts.
    3). Enable the FPV checks in sram_ctrl.
    
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
