import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5101"
version_tuple = (0, 0, 5101)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5101")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5010"
data_version_tuple = (0, 0, 5010)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5010")
except ImportError:
    pass
data_git_hash = "87285a2db401b932579a44b43d9691a8d04768b8"
data_git_describe = "v0.0-5010-g87285a2db"
data_git_msg = """\
commit 87285a2db401b932579a44b43d9691a8d04768b8
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Feb 18 15:57:05 2021 -0800

    [rtl/kmac] fix `right_encode(output_len)` for KDF
    
    this PR fixes the output length encoding that is padded by the
    kmac_keymgr module.
    The values should be exactly the same as the encoded keylength in
    kmac_core.sv, except the byte that contains the byte-length of the
    encoded value should be in the MSB position for right encoding instead
    of in the LSB position for left encoding.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
