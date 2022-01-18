import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9594"
version_tuple = (0, 0, 9594)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9594")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9472"
data_version_tuple = (0, 0, 9472)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9472")
except ImportError:
    pass
data_git_hash = "67b6a421ee94d6217977a60bcdf6abb5586fecce"
data_git_describe = "v0.0-9472-g67b6a421e"
data_git_msg = """\
commit 67b6a421ee94d6217977a60bcdf6abb5586fecce
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jan 18 08:05:55 2022 -0800

    [dv/otp_ctrl] Fix dai_err regression timeout
    
    This PR fixes timeout in dai_err in post_start. The post_start in
    cip_base_vseq uses dut_init which will start the otp_init. The OTP init
    won't work in this seq due to the errors, so we will have to re-backdoor
    program the entire OTP.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
