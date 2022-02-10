import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10234"
version_tuple = (0, 0, 10234)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10234")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10110"
data_version_tuple = (0, 0, 10110)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10110")
except ImportError:
    pass
data_git_hash = "8ae9bce3fabcda7b7c18f515f5ecf3de264c6c95"
data_git_describe = "v0.0-10110-g8ae9bce3f"
data_git_msg = """\
commit 8ae9bce3fabcda7b7c18f515f5ecf3de264c6c95
Author: TIM EWINS <tim.ewins@ensilica.com>
Date:   Wed Feb 2 15:32:36 2022 +0000

    [flash_ctrl] ADD TEST FOR SECRET PARTITIONS
    
    Test Secret Partitions Seeds to Key Manager
    and OTP Keys to Scramble function.
    tb.sv - Add VIF connections for OTP Key Model.
    
    Signed-off-by: TIM EWINS <tim.ewins@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
