import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8538"
version_tuple = (0, 0, 8538)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8538")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8426"
data_version_tuple = (0, 0, 8426)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8426")
except ImportError:
    pass
data_git_hash = "ec466390bb137c9defceb13322d85642526eb732"
data_git_describe = "v0.0-8426-gec466390b"
data_git_msg = """\
commit ec466390bb137c9defceb13322d85642526eb732
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 28 00:27:26 2021 +0000

    [util] Use pathlib throughout `util/check_dif_statuses.py`.
    
    This commit deprecates the use of the `os.path` module in favor of the
    `pathlib` module which is more consistently used acrossed `util`
    tooling.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
