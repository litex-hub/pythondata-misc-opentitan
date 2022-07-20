import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13192"
version_tuple = (0, 0, 13192)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13192")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13050"
data_version_tuple = (0, 0, 13050)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13050")
except ImportError:
    pass
data_git_hash = "1215e42fa2c629c4bac1a6e0fd53946acd09850a"
data_git_describe = "v0.0-13050-g1215e42fa2"
data_git_msg = """\
commit 1215e42fa2c629c4bac1a6e0fd53946acd09850a
Author: Miles Dai <milesdai@google.com>
Date:   Wed Jul 20 10:23:33 2022 -0400

    [ci/cdc] Fix cdc-only changes detection bug in CI
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
