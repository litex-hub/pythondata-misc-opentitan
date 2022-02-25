import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10557"
version_tuple = (0, 0, 10557)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10557")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10431"
data_version_tuple = (0, 0, 10431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10431")
except ImportError:
    pass
data_git_hash = "354bf05889db9c10d7a34f835cea2428dcdb8b64"
data_git_describe = "v0.0-10431-g354bf0588"
data_git_msg = """\
commit 354bf05889db9c10d7a34f835cea2428dcdb8b64
Author: TIM EWINS <tim.ewins@ensilica.com>
Date:   Tue Feb 15 15:21:36 2022 +0000

    [flash_ctrl] ADD TEST FOR THE RMA FEATURE
    
    Test the Flash RMA Functionality
    
    Fash Partitions are Erased, Programmed and then Wiped by the RMA.  After the RMA has completed,
    The test checks that SW Access to the FLASH is denied, and after a subsequent Reset, the Flash
    is confirmed to be set to data other than that previously programmed.
    Each run of the test performs 4 RMA cycles, each seperated by a Reset.
    
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
