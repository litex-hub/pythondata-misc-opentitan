import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5214"
version_tuple = (0, 0, 5214)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5214")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5123"
data_version_tuple = (0, 0, 5123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5123")
except ImportError:
    pass
data_git_hash = "53721b5ef9d7c655a5f9934ba7e08ccba17c8250"
data_git_describe = "v0.0-5123-g53721b5ef"
data_git_msg = """\
commit 53721b5ef9d7c655a5f9934ba7e08ccba17c8250
Author: Felix Miller <felix.miller@gi-de.com>
Date:   Thu Feb 18 02:48:15 2021 +0100

    [otbn] add optimized 384 bit Barrett mult for P-384
    
    Adds a variant for the 384 bit Barrett redcution
    based modular multiplication algorithm optimized
    for and limited to the NIST P-384 curve.
    
    Differences to generic version:
    - The multiplication sequences are inline to reduce
      move instructions and enbale different configurations
      for the multiplications
    - Use optimized multiplication sequences exploiting the
      special form of the P-384 modulus
    - Only a single conditional subtract of the modulus at
      the end
    
    Signed-off-by: Felix Miller <felix.miller@gi-de.com>

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
