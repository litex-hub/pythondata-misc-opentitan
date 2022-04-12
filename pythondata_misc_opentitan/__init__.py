import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11531"
version_tuple = (0, 0, 11531)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11531")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11405"
data_version_tuple = (0, 0, 11405)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11405")
except ImportError:
    pass
data_git_hash = "31d533e40f1864827f5c0d63d467ac639d8bca81"
data_git_describe = "v0.0-11405-g31d533e40"
data_git_msg = """\
commit 31d533e40f1864827f5c0d63d467ac639d8bca81
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Apr 12 10:32:36 2022 -0700

    [bazel] restrict specific to chip-level tests to DV sim
    
    Some tests can only run in DV simulation and therefor have been placed
    in `sw/device/test/sim_dv` to signify this. This updates the bazel rules
    for these tests to restrict them to the DV sim HW platform.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
