import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14244"
version_tuple = (0, 0, 14244)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14244")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14102"
data_version_tuple = (0, 0, 14102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14102")
except ImportError:
    pass
data_git_hash = "2abd786c664c619dab8a2538c479b3dcf03d9d54"
data_git_describe = "v0.0-14102-g2abd786c66"
data_git_msg = """\
commit 2abd786c664c619dab8a2538c479b3dcf03d9d54
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Sep 14 19:13:19 2022 -0700

    [bazel] reduce number of bitstreams included in the airgapped image
    
    The airgapped image requires an "initialized" bistreams cache in order
    for the bitstream cache "offline" mode to properly function. This
    reduces the number of bistreams included to just one to reduce the size
    fot he airgapped images.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
