import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14514"
version_tuple = (0, 0, 14514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14372"
data_version_tuple = (0, 0, 14372)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14372")
except ImportError:
    pass
data_git_hash = "1cfa4288c56887b5eb1b35d538a8dc5a8fef17cf"
data_git_describe = "v0.0-14372-g1cfa4288c5"
data_git_msg = """\
commit 1cfa4288c56887b5eb1b35d538a8dc5a8fef17cf
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Sep 15 15:29:56 2022 -0700

    [dependabot] add dependabot config file
    
    This adds a dependabot config file to trigger automatic updates to
    Python packages in response to #14941. This fixes #14956.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
