import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5620"
version_tuple = (0, 0, 5620)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5620")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5525"
data_version_tuple = (0, 0, 5525)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5525")
except ImportError:
    pass
data_git_hash = "41d815de155cb672b069155963395d104b1d71a6"
data_git_describe = "v0.0-5525-g41d815de1"
data_git_msg = """\
commit 41d815de155cb672b069155963395d104b1d71a6
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 29 15:07:02 2021 -0700

    [uvmdvgen] Fix has_interrupts in env_cfg
    
    This PR fixes `env_cfg.sv.tpl` to not generate interrupt related code
    when `has_interrupts` is not set.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
