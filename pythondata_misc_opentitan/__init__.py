import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10214"
version_tuple = (0, 0, 10214)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10214")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10090"
data_version_tuple = (0, 0, 10090)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10090")
except ImportError:
    pass
data_git_hash = "29c829a9e7eef8cb8af7e552933d365d80f2f23f"
data_git_describe = "v0.0-10090-g29c829a9e"
data_git_msg = """\
commit 29c829a9e7eef8cb8af7e552933d365d80f2f23f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 9 12:09:17 2022 -0800

    [dv/kmac] Fix TL integrity sequence error
    
    Because fatal alert can lock up `cfg_regwen`, and push sha3 fsm to error
    state. So we add these two fields to kmac_env_cfg.
    
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
