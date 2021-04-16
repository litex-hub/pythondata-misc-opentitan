import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5916"
version_tuple = (0, 0, 5916)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5916")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5821"
data_version_tuple = (0, 0, 5821)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5821")
except ImportError:
    pass
data_git_hash = "0caa13957ad09bb47d066653f2ce9a134b07fb98"
data_git_describe = "v0.0-5821-g0caa13957"
data_git_msg = """\
commit 0caa13957ad09bb47d066653f2ce9a134b07fb98
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 16 12:48:38 2021 +0100

    [keymgr,lint] Waive some Verilator warnings about array accesses
    
    "Fixing" this in the RTL would be hard. The problem is that you'd need
    to make some 2-bit signals to represent the enum entries.
    Unfortunately, AscentLint (the lint tool that we use for signoff)
    doesn't accept code that extracts bits from enum values without an
    explicit concatenation. So you end up having to write something like
    this for each enum entry:
    
      localparam bit [2:0] OpAdvanceBits = {OpAdvance};
      localparam bit [1:0] ShortOpAdvance = OpAdvanceBits[1:0];
    
    which is getting a bit ridiculous. Just waive the warning.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
