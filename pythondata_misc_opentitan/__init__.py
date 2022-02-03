import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10022"
version_tuple = (0, 0, 10022)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10022")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9898"
data_version_tuple = (0, 0, 9898)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9898")
except ImportError:
    pass
data_git_hash = "5e2635e91b6562cb7bb6e5e9da9d8f0043eae75e"
data_git_describe = "v0.0-9898-g5e2635e91"
data_git_msg = """\
commit 5e2635e91b6562cb7bb6e5e9da9d8f0043eae75e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sat Jan 29 14:16:22 2022 -0800

    [dv/hmac] Fix hmac fcov bin and a stress_all_with_rand_reset issue
    
    1). Fix max outstanding item from 2 to 1.
    2). Stress_all_with_rand_reset does not use `apply_reset`, so added a
      line of logic to set back the cfg flag before issuing the concurrent
      reset.
    
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
