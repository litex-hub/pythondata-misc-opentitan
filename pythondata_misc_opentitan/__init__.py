import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9647"
version_tuple = (0, 0, 9647)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9647")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9525"
data_version_tuple = (0, 0, 9525)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9525")
except ImportError:
    pass
data_git_hash = "40203d2c65a2b1e1986ed31292bea8e17e9fb4e1"
data_git_describe = "v0.0-9525-g40203d2c6"
data_git_msg = """\
commit 40203d2c65a2b1e1986ed31292bea8e17e9fb4e1
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jan 14 15:29:19 2022 +0100

    [aes] Fix CSR test exclusions for key, IV and data input registers
    
    Just like the data output registers, these are cleared with pseudo-
    random data after reset meaning they should be excluded from the HW
    reset tests.
    
    This resolves lowRISC/OpenTitan#10081.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
