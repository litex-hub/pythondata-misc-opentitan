import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14695"
version_tuple = (0, 0, 14695)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14695")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14553"
data_version_tuple = (0, 0, 14553)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14553")
except ImportError:
    pass
data_git_hash = "5db82833a4e9207e59b44236947b4548156f947b"
data_git_describe = "v0.0-14553-g5db82833a4"
data_git_msg = """\
commit 5db82833a4e9207e59b44236947b4548156f947b
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Oct 11 17:47:15 2022 +0200

    [crypto] Bugfix for RSA-4096 encryption.
    
    Fixes #15331
    
    The number of bytes needed for RSA-4096 was miscalculated in rsa.s (it
    should be 512 bytes, not 480). This fixes the bug and also adds some
    small cleanups (whole-word writes to DMEM for n_limbs and mode, and
    .balign directives for the OTBN data).
    
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
