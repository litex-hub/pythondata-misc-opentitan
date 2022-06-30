import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12902"
version_tuple = (0, 0, 12902)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12902")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12760"
data_version_tuple = (0, 0, 12760)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12760")
except ImportError:
    pass
data_git_hash = "808fb6435657b295f856b790cb00193dfd3fab96"
data_git_describe = "v0.0-12760-g808fb64356"
data_git_msg = """\
commit 808fb6435657b295f856b790cb00193dfd3fab96
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jun 28 22:00:36 2022 -0700

    [dv,chip,hmac_idle] Add chip_sw_hmac_enc_idle test
    
    Develop this along the line of aes_idle. Check against both hmac
    processing steps used in chip_sw_hmac_enc_test.
    Share some of the reference data and expected digests between these
    two tests via hmac_testutils.
    Add this hmac and the otbn idle tests to chip_sw_clkmgr_idle_trans
    testpoint.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
