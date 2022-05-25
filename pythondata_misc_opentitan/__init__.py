import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12302"
version_tuple = (0, 0, 12302)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12302")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12174"
data_version_tuple = (0, 0, 12174)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12174")
except ImportError:
    pass
data_git_hash = "3a25971363d2d3dc7479c2b12abd57723a0699d7"
data_git_describe = "v0.0-12174-g3a2597136"
data_git_msg = """\
commit 3a25971363d2d3dc7479c2b12abd57723a0699d7
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue May 24 14:02:13 2022 -0700

    [dvsim] Revert #12761 to build SW with meson
    
    Since switching dvsim.py to build SW with Bazel (instead of meson),
    private CI job runtimes have increased. This is detailed in #12840. As a
    temporary fix, this commit reverts #12761, and switch dvsim.py back to
    using meson to build SW images.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
