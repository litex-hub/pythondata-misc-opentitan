import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13259"
version_tuple = (0, 0, 13259)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13259")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13117"
data_version_tuple = (0, 0, 13117)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13117")
except ImportError:
    pass
data_git_hash = "9a396db0aebc2315759fdec5b3a402f320d3d877"
data_git_describe = "v0.0-13117-g9a396db0ae"
data_git_msg = """\
commit 9a396db0aebc2315759fdec5b3a402f320d3d877
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Mon Jul 25 09:12:09 2022 -0700

    fix(rv_plic): Typo
    
    Typo `alerts[0]`. It should be `alerts[i]`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
