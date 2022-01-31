import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9925"
version_tuple = (0, 0, 9925)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9925")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9801"
data_version_tuple = (0, 0, 9801)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9801")
except ImportError:
    pass
data_git_hash = "a45456ab3434369c06d62bc249970e5a8669bd70"
data_git_describe = "v0.0-9801-ga45456ab3"
data_git_msg = """\
commit a45456ab3434369c06d62bc249970e5a8669bd70
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Jan 17 10:25:16 2022 +0000

    [sw,crypto] Reject large signatures in RSA verification.
    
    Modify sigverify and the crypto library RSA implementation to check that
    signatures are within bounds and reject them otherwise.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
