import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9416"
version_tuple = (0, 0, 9416)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9416")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9298"
data_version_tuple = (0, 0, 9298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9298")
except ImportError:
    pass
data_git_hash = "827b23227e7ef0beaafe73920cba51a56e8e0afa"
data_git_describe = "v0.0-9298-g827b23227"
data_git_msg = """\
commit 827b23227e7ef0beaafe73920cba51a56e8e0afa
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jan 10 11:23:50 2022 -0800

    [pinmux/doc] Update docs
    
    Fix #9953
    
    Indicate that all pad attribute CSRs have WARL access, and make a note
    that the pad attributes will be temporarily forced to 0 on the JTAG IOs
    when they are activated.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
