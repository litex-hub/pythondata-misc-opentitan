import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11383"
version_tuple = (0, 0, 11383)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11383")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11257"
data_version_tuple = (0, 0, 11257)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11257")
except ImportError:
    pass
data_git_hash = "6d2f7e6e4a7e66787f23e04b954eb98e2f92c3d4"
data_git_describe = "v0.0-11257-g6d2f7e6e4"
data_git_msg = """\
commit 6d2f7e6e4a7e66787f23e04b954eb98e2f92c3d4
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Apr 4 17:25:03 2022 -0700

    [adc_ctrl] Fix adc interrupt synchronization
    
    - fixes #11759
    - switch to prim_reqack instead of prim_pulse_sync
    - since many events can occur during low power, split
      the sync source into staging and request.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
