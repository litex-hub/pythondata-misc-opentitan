import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14794"
version_tuple = (0, 0, 14794)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14794")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14652"
data_version_tuple = (0, 0, 14652)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14652")
except ImportError:
    pass
data_git_hash = "484086eec0115826ca5ee26ab7bef956bd1eb190"
data_git_describe = "v0.0-14652-g484086eec0"
data_git_msg = """\
commit 484086eec0115826ca5ee26ab7bef956bd1eb190
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 7 17:28:06 2022 +0200

    [crypto] Safely generate the P-256 secret scalar and random keys.
    
    Previously, the secret scalar k was simply fetched from RND, but when
    reduced modulo the curve order the value will be biased. For this
    reason, the FIPS spec requires generating the secret scalar from a
    larger (320-bit) seed, and additionally ensuring it is nonzero.
    Generation of the secret key from a random seed is very similar.
    
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
