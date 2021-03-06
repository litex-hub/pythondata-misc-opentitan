import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5939"
version_tuple = (0, 0, 5939)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5939")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5844"
data_version_tuple = (0, 0, 5844)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5844")
except ImportError:
    pass
data_git_hash = "dcee03a96bea3246a99de80c03055312015843ca"
data_git_describe = "v0.0-5844-gdcee03a96"
data_git_msg = """\
commit dcee03a96bea3246a99de80c03055312015843ca
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Apr 16 14:52:24 2021 -0700

    [dv/dv_macros] Fix DV_PRINT_ARR_CONTENTS
    
    For array `arr` with a single value 42, DV_PRINT_ARR_CONTENTS
    should print `arr[0] = 42 (0x2a)`; it currently prints
    `arr[0] = 0x42[0x2a]`.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
