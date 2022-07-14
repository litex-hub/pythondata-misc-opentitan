import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13071"
version_tuple = (0, 0, 13071)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13071")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12929"
data_version_tuple = (0, 0, 12929)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12929")
except ImportError:
    pass
data_git_hash = "8c853f05a104abbb900caf22917be9f19e6da46e"
data_git_describe = "v0.0-12929-g8c853f05a1"
data_git_msg = """\
commit 8c853f05a104abbb900caf22917be9f19e6da46e
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Jun 28 16:30:43 2022 +0100

    [crypto] Change AES-GCM GHASH implementation to use 4-bit windows.
    
    This provides significant space savings as well as speed savings for
    small inputs, although large inputs will be substantially slower.
    Specifically, the constant overhead per encryption is about 10x more
    (17k vs 170k cycles) for 8-bit windows because of computing the product
    table, but GHASH is about twice as fast (20k vs 10k cycles). We have to
    compute 1 GHASH per plaintext or aad block, so eventually the speedup in
    GHASH overtakes the higher overhead. However, this only overtaking
    happens at about 256 bytes of plaintext + aad, which is already around
    300k cycles. Since large inputs will need to be chunked to meet latency
    requirements anyway, it seems like the space and speed for small inputs
    are worth some slowdown in larger inputs.
    
    Also includes a few code fixes from code review comments.
    
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
