import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12972"
version_tuple = (0, 0, 12972)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12972")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12830"
data_version_tuple = (0, 0, 12830)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12830")
except ImportError:
    pass
data_git_hash = "f3d189cf5d9ef1d3b0e5c88231400631962932a0"
data_git_describe = "v0.0-12830-gf3d189cf5d"
data_git_msg = """\
commit f3d189cf5d9ef1d3b0e5c88231400631962932a0
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Jun 29 12:52:04 2022 -0400

    [util/design] Encode bit width in filename of OTP vmem file
    
    The script now supports a templated output name parameter. This PR also
    updates rules/autogen.bzl, where the script is called.
    
    This change will enable hw/ip/rom_ctrl/util/gen_vivado_mem_image.py to
    parse the memory width from the filename. See discussion in #10867.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
