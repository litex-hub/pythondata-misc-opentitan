import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11023"
version_tuple = (0, 0, 11023)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11023")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10897"
data_version_tuple = (0, 0, 10897)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10897")
except ImportError:
    pass
data_git_hash = "4048a11acbddd921532f3d205920ddead7d5fb1b"
data_git_describe = "v0.0-10897-g4048a11ac"
data_git_msg = """\
commit 4048a11acbddd921532f3d205920ddead7d5fb1b
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Mar 16 16:31:14 2022 -0700

    [dv/otp] Update sec_cm testplan
    
    This PR updates the auto-generated sec_cmd testplan to include matching
    DV tests.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
