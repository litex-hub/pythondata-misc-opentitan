import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14770"
version_tuple = (0, 0, 14770)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14770")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14628"
data_version_tuple = (0, 0, 14628)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14628")
except ImportError:
    pass
data_git_hash = "bcbae4445d5e6677ffe3cb8a6b939da7170bbabd"
data_git_describe = "v0.0-14628-gbcbae4445d"
data_git_msg = """\
commit bcbae4445d5e6677ffe3cb8a6b939da7170bbabd
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 14 15:04:15 2022 +0200

    [crypto] Fix bug in ECDSA-P256 scalar inversion.
    
    Fixes a recently introduced bug in ECDSA-P256 signatures; the scalar
    inversion routine handles scalars in plaintext, so the shares need to be
    combined in order to use it. Eventually we should use a more heavily
    protected implementation (see #15507) but for now this just fixes the
    bug by combining shares.
    
    This commit also updates the p256 signature test to use both shares, so
    that this type of bug will be caught faster in the future.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
