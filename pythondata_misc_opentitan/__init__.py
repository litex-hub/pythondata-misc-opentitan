import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12560"
version_tuple = (0, 0, 12560)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12560")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12418"
data_version_tuple = (0, 0, 12418)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12418")
except ImportError:
    pass
data_git_hash = "0b853a515a376d2966f51d30b65e7977d7154d20"
data_git_describe = "v0.0-12418-g0b853a515"
data_git_msg = """\
commit 0b853a515a376d2966f51d30b65e7977d7154d20
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jun 1 14:46:31 2022 -0700

    [dv/chip] walkthrough test fixes
    
    1). Fix typo in walkthrough test: transtition -> transition.
    2). Fix bazel sw_image path, adding a `sim_dv` folder in the path.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
