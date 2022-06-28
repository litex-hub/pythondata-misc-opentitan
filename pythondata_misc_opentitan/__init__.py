import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12864"
version_tuple = (0, 0, 12864)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12864")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12722"
data_version_tuple = (0, 0, 12722)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12722")
except ImportError:
    pass
data_git_hash = "179558354cbdf7a844a9c3634b332b50c963d24c"
data_git_describe = "v0.0-12722-g179558354c"
data_git_msg = """\
commit 179558354cbdf7a844a9c3634b332b50c963d24c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jun 27 15:42:31 2022 -0700

    [dv/otp_ctrl] Fix lc_dft_en failures
    
    This PR fixes the regression failures when lc_dft_en is set to On and DV
    did not expect it to return d_error.
    This case is hard to align on the scoreboard side because it is timing
    sensetive regarding the d_channel and a_channel.
    Because this case is not likely to happen in chip level (lc_dft_en
    cannot be switched on and off on the fly), I added a TODO to support
    checking that in otp_ctrl_test_access sequence.
    
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
