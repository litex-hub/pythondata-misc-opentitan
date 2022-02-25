import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10552"
version_tuple = (0, 0, 10552)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10552")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10426"
data_version_tuple = (0, 0, 10426)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10426")
except ImportError:
    pass
data_git_hash = "419d7b14251c2aa8f81b71ff8efde9b31223f52f"
data_git_describe = "v0.0-10426-g419d7b142"
data_git_msg = """\
commit 419d7b14251c2aa8f81b71ff8efde9b31223f52f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 23 17:14:04 2022 -0800

    [fpv/pinmux] Pinmux FPV tb fix
    
    This PR fixes pinmux FPV:
    
    1). Blackbox usb module because we only check connectivity here.
    2). Disable assertions for `SyncCheckTransients*` because in formal we
      do not constraint inputs.
    3). Updated lc_ctrl_pkg::On/Off to not use `mubi4_test_true_strict`
      function.
    4). Update a few design input related assertions to use assumptions.
    
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
