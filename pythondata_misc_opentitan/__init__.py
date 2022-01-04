import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9321"
version_tuple = (0, 0, 9321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9204"
data_version_tuple = (0, 0, 9204)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9204")
except ImportError:
    pass
data_git_hash = "8b675981e9a9f2a7ebadc2f7964e4b2437bacce6"
data_git_describe = "v0.0-9204-g8b675981e"
data_git_msg = """\
commit 8b675981e9a9f2a7ebadc2f7964e4b2437bacce6
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Dec 16 18:08:59 2021 -0800

    [sw/dif] Add `toggle_to_bool()` and `bool_to_toggle()` to DIF base.
    
    Several DIF libraries had redefined the same logic to translate
    `dif_toggle_t` types to/from bool types. This commit adds one shared
    implementation of said functions, and removes the duplicates across
    individual DIF libraries.
    
    This partially addresses a task item in #9036.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
