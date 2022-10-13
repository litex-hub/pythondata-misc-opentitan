import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14736"
version_tuple = (0, 0, 14736)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14736")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14594"
data_version_tuple = (0, 0, 14594)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14594")
except ImportError:
    pass
data_git_hash = "daad15d95d10895a2a2260b0bbbdfec807ad5c15"
data_git_describe = "v0.0-14594-gdaad15d95d"
data_git_msg = """\
commit daad15d95d10895a2a2260b0bbbdfec807ad5c15
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 13 08:38:10 2022 -0700

    [dv/otp] Fix stress_all_with_rand_reset nightly failure
    
    This PR fixes the stress_all_with_rand_reset test failure when the base
    sequence access all CSRs to check their default values after reset.
    The current testbench did not enable `dft_en`, so the test failed due to
    illegal access.
    
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
