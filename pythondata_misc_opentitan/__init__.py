import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13024"
version_tuple = (0, 0, 13024)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13024")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12882"
data_version_tuple = (0, 0, 12882)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12882")
except ImportError:
    pass
data_git_hash = "210577402e9804e997003af40ef55eeffc360687"
data_git_describe = "v0.0-12882-g210577402e"
data_git_msg = """\
commit 210577402e9804e997003af40ef55eeffc360687
Author: Hugo McNally <hugo.mcnally@gmail.com>
Date:   Mon Jun 20 15:01:19 2022 +0100

    [doc] Inserted header anchors/links.
    
    Signed-off-by: Hugo McNally <hugo.mcnally@gmail.com>

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
