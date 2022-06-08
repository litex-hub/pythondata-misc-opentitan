import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12564"
version_tuple = (0, 0, 12564)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12564")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12422"
data_version_tuple = (0, 0, 12422)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12422")
except ImportError:
    pass
data_git_hash = "1995394f8a8e9447e4f4a9b17753f3b1cd22ece8"
data_git_describe = "v0.0-12422-g1995394f8"
data_git_msg = """\
commit 1995394f8a8e9447e4f4a9b17753f3b1cd22ece8
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Jun 3 18:09:39 2022 -0700

    [cryptolib/aes] Add NIST test vector.
    
    Switch test case to use a NIST test vector to make the test case easier to
    audit. The test was previously not passing on Verilator/FPGA targets.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
