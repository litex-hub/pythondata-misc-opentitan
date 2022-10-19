import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14839"
version_tuple = (0, 0, 14839)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14839")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14697"
data_version_tuple = (0, 0, 14697)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14697")
except ImportError:
    pass
data_git_hash = "feac7a5778efe53389595d1302fd3c6457663832"
data_git_describe = "v0.0-14697-gfeac7a5778"
data_git_msg = """\
commit feac7a5778efe53389595d1302fd3c6457663832
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 19 08:40:14 2022 -0400

    [ci] Fix typo in dependabot config
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
