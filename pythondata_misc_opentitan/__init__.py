import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8449"
version_tuple = (0, 0, 8449)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8449")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8337"
data_version_tuple = (0, 0, 8337)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8337")
except ImportError:
    pass
data_git_hash = "00589e0551f74f98910535f9e211e5dee6cb381c"
data_git_describe = "v0.0-8337-g00589e055"
data_git_msg = """\
commit 00589e0551f74f98910535f9e211e5dee6cb381c
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Oct 25 18:27:11 2021 +0100

    [sw] Set up licensing for RSA-3072.
    
    Copy the dcrypto license into lib/crypto and exempt rsa_3072.s from the
    automated license check.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
