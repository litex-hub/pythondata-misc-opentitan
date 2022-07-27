import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13278"
version_tuple = (0, 0, 13278)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13278")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13136"
data_version_tuple = (0, 0, 13136)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13136")
except ImportError:
    pass
data_git_hash = "a04d74569382e62eb720d66909c8dedc1f6aeb93"
data_git_describe = "v0.0-13136-ga04d745693"
data_git_msg = """\
commit a04d74569382e62eb720d66909c8dedc1f6aeb93
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jul 25 18:04:14 2022 -0700

    [dv/kmac] Fix assertion failures in shadow reg
    
    This PR disable a few assertions when shadow_reg error fires.
    Because the kmac will go to terminal state.
    
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
