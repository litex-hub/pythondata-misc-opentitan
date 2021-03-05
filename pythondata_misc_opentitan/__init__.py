import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5257"
version_tuple = (0, 0, 5257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5166"
data_version_tuple = (0, 0, 5166)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5166")
except ImportError:
    pass
data_git_hash = "4c609f8ad262174d4c802cb3f8624840488ec38b"
data_git_describe = "v0.0-5166-g4c609f8ad"
data_git_msg = """\
commit 4c609f8ad262174d4c802cb3f8624840488ec38b
Author: Michael Schaffner <msf@google.com>
Date:   Thu Mar 4 18:20:43 2021 -0800

    [chip/dv] Fix OTP preloading issues in chip DV environment
    
    This moves OTP preloading into the chip_base_vseq such that all tests
    correctly preload the OTP with the correct LC state.
    
    This also adds some more CSR exclusions, as now the OTP and LC
    controllers populate these CSRs with nonzero values upon init.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
