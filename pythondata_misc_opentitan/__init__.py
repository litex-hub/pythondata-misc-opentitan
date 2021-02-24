import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5130"
version_tuple = (0, 0, 5130)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5130")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5039"
data_version_tuple = (0, 0, 5039)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5039")
except ImportError:
    pass
data_git_hash = "76f567c9a40f0a2ce4d3a1aabaf579d74e7312da"
data_git_describe = "v0.0-5039-g76f567c9a"
data_git_msg = """\
commit 76f567c9a40f0a2ce4d3a1aabaf579d74e7312da
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Feb 24 09:16:58 2021 -0800

    [dv/kmac] fix regression failures
    
    requested output length foor SHAKE256 test_vectors test can go over 136B
    (the keccak block size), need disable existing output length constraints
    to avoid constraint failures midway through the test.
    
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
