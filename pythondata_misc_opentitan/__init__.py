import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9880"
version_tuple = (0, 0, 9880)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9880")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9756"
data_version_tuple = (0, 0, 9756)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9756")
except ImportError:
    pass
data_git_hash = "fd557a694166a981c3e5e3c70a177461d29f3226"
data_git_describe = "v0.0-9756-gfd557a694"
data_git_msg = """\
commit fd557a694166a981c3e5e3c70a177461d29f3226
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 27 12:33:52 2022 -0800

    [dv/reggen] Adjust hier_path input for close source OTP tb
    
    This PR slightly adjust optional input `hier_path` for ip_blocks,
    by removing the default `u_reg` path, so close source OTP will have
    the correct hier_path.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
