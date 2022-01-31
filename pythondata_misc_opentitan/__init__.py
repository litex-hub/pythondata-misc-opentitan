import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9918"
version_tuple = (0, 0, 9918)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9918")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9794"
data_version_tuple = (0, 0, 9794)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9794")
except ImportError:
    pass
data_git_hash = "791f7d7f5cedb45c112ee99d0c5f410898e38b6d"
data_git_describe = "v0.0-9794-g791f7d7f5"
data_git_msg = """\
commit 791f7d7f5cedb45c112ee99d0c5f410898e38b6d
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Jan 25 15:59:39 2022 +0000

    [kmac_app_agt, dv] Randmoizing agent configuration
    
    Many of the agent configuration variables are random variables. The
    agent configuration needs to be randomized for the variables to be
    initialised to hit all coverage corners.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
