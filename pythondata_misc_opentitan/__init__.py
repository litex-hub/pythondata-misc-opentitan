import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8937"
version_tuple = (0, 0, 8937)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8937")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8825"
data_version_tuple = (0, 0, 8825)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8825")
except ImportError:
    pass
data_git_hash = "2e0a17b3b60bc40565ebc6d9a2564f604f0c6564"
data_git_describe = "v0.0-8825-g2e0a17b3b"
data_git_msg = """\
commit 2e0a17b3b60bc40565ebc6d9a2564f604f0c6564
Author: Dror Kabely <dror.kabely@opentitan.org>
Date:   Wed Dec 1 13:59:41 2021 +0200

    [dv/otp_ctrl] added post_pwr_otp_init to callback and base vseq
    
    Signed-off-by: Dror Kabely <dror.kabely@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
