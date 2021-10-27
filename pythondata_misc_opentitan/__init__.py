import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8470"
version_tuple = (0, 0, 8470)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8470")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8358"
data_version_tuple = (0, 0, 8358)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8358")
except ImportError:
    pass
data_git_hash = "a24806411534f332cbfe7aac37f7b3fd7672ac01"
data_git_describe = "v0.0-8358-ga24806411"
data_git_msg = """\
commit a24806411534f332cbfe7aac37f7b3fd7672ac01
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 26 17:43:55 2021 +0100

    [otbn,sw] Use weak symbols to shrink data in rsa_verify_3072_test
    
    The code in rsa_verify_3072.s expects various input and output arrays.
    The code in rsa_verify_3072_test.s wants to initialise these arrays
    with known values. To do that, it was declaring another copy of each
    array (with the known values) and copying the values across.
    
    Rather than doing that, use weak symbols and per-data sections in
    rsa_verify_3072.s and then override them in the test file.
    
    Something like this is needed if you want to get the total externally
    visible data down below 2kb.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
