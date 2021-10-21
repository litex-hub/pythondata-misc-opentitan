import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8366"
version_tuple = (0, 0, 8366)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8366")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8254"
data_version_tuple = (0, 0, 8254)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8254")
except ImportError:
    pass
data_git_hash = "b8ddad8f47513e994d13765d4232bf2616c393a0"
data_git_describe = "v0.0-8254-gb8ddad8f4"
data_git_msg = """\
commit b8ddad8f47513e994d13765d4232bf2616c393a0
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 20 10:25:54 2021 -0400

    [sw/silicon_creator] Move length checks from manifest to boot_policy
    
    Minimum and maximum allowed lengths for ROM_EXT and first owner boot
    stage images will be different. This change adds individual constants
    for both stages and moves related checks from manifest.h to mask ROM and
    ROM_EXT boot policy implementations.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
