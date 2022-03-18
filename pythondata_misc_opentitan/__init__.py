import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10970"
version_tuple = (0, 0, 10970)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10970")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10844"
data_version_tuple = (0, 0, 10844)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10844")
except ImportError:
    pass
data_git_hash = "dcd9d110d6706d8acf1c14c21004cb4d13da8da8"
data_git_describe = "v0.0-10844-gdcd9d110d"
data_git_msg = """\
commit dcd9d110d6706d8acf1c14c21004cb4d13da8da8
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Thu Feb 17 17:05:09 2022 +0000

    [hmac_enc, tests] Introduce the HMAC chip level test (non-irq)
    
    This change uses HMAC example vector from:
    https://csrc.nist.gov/CSRC/media/Projects/
    Cryptographic-Standards-and-Guidelines/documents/
    examples/HMAC_SHA256.pdf
    
    Key length = 100
    Tag length = 32
    
    This example vector has key length larger, and not aligned to the
    block size. This makes it well suited to check the basic conformance
    to the HMAC specification, which states that when key is larger than
    the block size, it must be hashed to produce a block sized key.
    
    Please see:
    https://csrc.nist.gov/csrc/media/publications/fips/198/archive/
    2002-03-06/documents/fips-198a.pdf
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
