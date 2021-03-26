import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5604"
version_tuple = (0, 0, 5604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5509"
data_version_tuple = (0, 0, 5509)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5509")
except ImportError:
    pass
data_git_hash = "44fe217af660b1abbe22fa00e70583482f096871"
data_git_describe = "v0.0-5509-g44fe217af"
data_git_msg = """\
commit 44fe217af660b1abbe22fa00e70583482f096871
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 26 11:22:05 2021 +0000

    [csrng] Fix some width mismatches
    
    These cause lint errors from Verilator. Most of the changes are
    mechanical, but I've changed the left shift that computes
    concat_outblk_shifted_value to add the BlkLen zeros at the bottom
    explicitly (I think we might have been silently dropping the top block
    before).
    
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
