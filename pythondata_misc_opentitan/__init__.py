import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5209"
version_tuple = (0, 0, 5209)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5209")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5118"
data_version_tuple = (0, 0, 5118)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5118")
except ImportError:
    pass
data_git_hash = "c8b3333ec9a5fd550198d2772926227005e8f4e0"
data_git_describe = "v0.0-5118-gc8b3333ec"
data_git_msg = """\
commit c8b3333ec9a5fd550198d2772926227005e8f4e0
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Mar 2 17:19:52 2021 -0800

    [rtl/lc_ctrl] Fix jtag d_error
    
    When I try to use DMI to access LC_CTRL CSR, I always get a `d_error`.
    The error is coming from this check: https://github.com/lowRISC/opentitan/blob/master/hw/ip/tlul/rtl/tlul_pkg.sv#L142
    I believe it is related to default value for tap's tl_i.a_user.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
