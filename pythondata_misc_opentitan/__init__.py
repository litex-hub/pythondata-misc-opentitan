import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11037"
version_tuple = (0, 0, 11037)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11037")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10911"
data_version_tuple = (0, 0, 10911)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10911")
except ImportError:
    pass
data_git_hash = "63c4132d4cab8cd34afc239c8111f25187816b9a"
data_git_describe = "v0.0-10911-g63c4132d4"
data_git_msg = """\
commit 63c4132d4cab8cd34afc239c8111f25187816b9a
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Mar 22 20:55:13 2022 -0700

    [verix] Add more reports for debugging
    
    Add clock domains, matrix to the reports to debug.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
