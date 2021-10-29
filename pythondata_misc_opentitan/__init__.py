import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8531"
version_tuple = (0, 0, 8531)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8531")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8419"
data_version_tuple = (0, 0, 8419)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8419")
except ImportError:
    pass
data_git_hash = "135a6c4e1fd679e521503be004bd83308de0a8a7"
data_git_describe = "v0.0-8419-g135a6c4e1"
data_git_msg = """\
commit 135a6c4e1fd679e521503be004bd83308de0a8a7
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Oct 26 11:09:07 2021 +0100

    [sw] Clarify bounds for Barrett multiplication in ECDSA-P256.
    
    The Barrett implementation can accept one operand that is greater than
    the modulus, which allows us to not reduce the digest modulo n before
    calling p256_sign.
    
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
