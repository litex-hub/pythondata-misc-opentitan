import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5758"
version_tuple = (0, 0, 5758)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5758")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5663"
data_version_tuple = (0, 0, 5663)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5663")
except ImportError:
    pass
data_git_hash = "de7eba3d7af1f55b7bda8104152b4240f3d37456"
data_git_describe = "v0.0-5663-gde7eba3d7"
data_git_msg = """\
commit de7eba3d7af1f55b7bda8104152b4240f3d37456
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Mar 22 14:18:38 2021 -0700

    [csrng/entropy_src] fix for #4601
    
    Inter-module signals to prevent power spikes.
    Changed permissions for several files to not be executable.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
