import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11190"
version_tuple = (0, 0, 11190)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11190")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11064"
data_version_tuple = (0, 0, 11064)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11064")
except ImportError:
    pass
data_git_hash = "e1e3c63f0150137100b4b63ec4214088cd8d1239"
data_git_describe = "v0.0-11064-ge1e3c63f0"
data_git_msg = """\
commit e1e3c63f0150137100b4b63ec4214088cd8d1239
Author: Miles Dai <milesdai@google.com>
Date:   Tue Mar 22 16:40:52 2022 -0400

    [mask_rom/e2e] Add boot success and no rom_ext signature tests
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
