import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13065"
version_tuple = (0, 0, 13065)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13065")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12923"
data_version_tuple = (0, 0, 12923)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12923")
except ImportError:
    pass
data_git_hash = "bed33ef9b2340cc6ab1873f515251af8297a4af0"
data_git_describe = "v0.0-12923-gbed33ef9b2"
data_git_msg = """\
commit bed33ef9b2340cc6ab1873f515251af8297a4af0
Author: Dan McArdle <dmcardle@google.com>
Date:   Tue Jul 12 12:37:38 2022 -0400

    [bazel] Add functest that uses OTP-spliced bitstream
    
    Add a new CW310-specific functest:
    //sw/device/silicon_creator/mask_rom:e2e_bootup_success_otp_dev.
    
    This new functest uses //hw/bitstream:mask_rom_otp_dev, which is the
    Mask ROM bitstream after splicing in the OTP Dev image, replacing the
    OTP RMA image.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
