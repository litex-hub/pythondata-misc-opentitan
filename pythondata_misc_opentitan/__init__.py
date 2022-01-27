import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9848"
version_tuple = (0, 0, 9848)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9848")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9724"
data_version_tuple = (0, 0, 9724)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9724")
except ImportError:
    pass
data_git_hash = "8a35814ef0db693f67549738f46087d57dcb5251"
data_git_describe = "v0.0-9724-g8a35814ef"
data_git_msg = """\
commit 8a35814ef0db693f67549738f46087d57dcb5251
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jan 26 07:20:04 2022 -0800

    [bazel] start running in CI and warning
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
