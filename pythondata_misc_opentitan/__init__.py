import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5262"
version_tuple = (0, 0, 5262)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5262")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5168"
data_version_tuple = (0, 0, 5168)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5168")
except ImportError:
    pass
data_git_hash = "95cea45d4f2912324a0fba32e97e2f87a14bea03"
data_git_describe = "v0.0-5168-g95cea45d4"
data_git_msg = """\
commit 95cea45d4f2912324a0fba32e97e2f87a14bea03
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Mar 2 08:54:01 2021 +0100

    [aes] Interface CSRNG through EDN
    
    This commit interfaces the AES unit with CSRNG/EDN to reseed the internal
    PRNGs for clearing and masking. Since on the SCA platform, we don't have
    enough resources to implement CSRNG and EDN, a new parameter
    SecSkipPRNGReseeding is added to skip reseeding requests on the SCA
    platform.
    
    If the reseeding was done with deterministic input instead of entropy
    provided by CSRNG, this would result in quickly repeating, deterministic
    PRNG output which is not suitable for evaluating SCA resistance.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post94"
tool_version_tuple = (0, 0, 94)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post94")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
