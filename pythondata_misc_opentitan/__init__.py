import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14386"
version_tuple = (0, 0, 14386)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14386")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14244"
data_version_tuple = (0, 0, 14244)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14244")
except ImportError:
    pass
data_git_hash = "9d0b3194bc63906274478d3c96a6e57d751021bc"
data_git_describe = "v0.0-14244-g9d0b3194bc"
data_git_msg = """\
commit 9d0b3194bc63906274478d3c96a6e57d751021bc
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Sep 22 09:56:24 2022 -0700

    fix(kmac): Check SHA3 done loosely for false value
    
    Related Issue: https://github.com/lowRISC/opentitan/issues/15002
    
    KMAC checks `sha3_done` false value strictly. It opened the attackers
    making KMAC not finished and keep feeding messages.
    
    By checking `sha3_done` loosely in this commit, the state always moves
    to next state when `sha3_absorbed` is true.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
