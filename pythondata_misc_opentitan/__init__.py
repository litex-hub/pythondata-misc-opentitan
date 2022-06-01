import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12441"
version_tuple = (0, 0, 12441)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12441")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12299"
data_version_tuple = (0, 0, 12299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12299")
except ImportError:
    pass
data_git_hash = "672f9167e3b7fc2593eb33a552038b1bceec5aac"
data_git_describe = "v0.0-12299-g672f9167e"
data_git_msg = """\
commit 672f9167e3b7fc2593eb33a552038b1bceec5aac
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Mon May 30 12:15:47 2022 +0100

    [flash_ctrl] Add oob_err exclusions
    
    Add lines 45 and 49 of flash_ctrl_erase.sv file to exclusions due
    to oob error.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
