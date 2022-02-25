import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10542"
version_tuple = (0, 0, 10542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10416"
data_version_tuple = (0, 0, 10416)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10416")
except ImportError:
    pass
data_git_hash = "0b725cd8ccd980e0dd8b2168de766bc4c34368ea"
data_git_describe = "v0.0-10416-g0b725cd8c"
data_git_msg = """\
commit 0b725cd8ccd980e0dd8b2168de766bc4c34368ea
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Feb 3 13:57:13 2022 +0000

    [sw,crypto] Test vector setup for ECDSA-P256 verify.
    
    Based on the existing setup for RSA-3072, this should allow us to easily
    switch out test vector sets and produce random test vectors. For now,
    there are just two simple tests as the hard-coded defaults.
    
    Also add Bazel rules to build the ECDSA-P256 tests (not yet possible for
    RSA due to build conflicts in the OTBN code).
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
