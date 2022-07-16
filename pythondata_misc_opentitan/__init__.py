import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13137"
version_tuple = (0, 0, 13137)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13137")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12995"
data_version_tuple = (0, 0, 12995)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12995")
except ImportError:
    pass
data_git_hash = "4a949ee43da5ce26e1c8d338a1f1cbb370a0b82e"
data_git_describe = "v0.0-12995-g4a949ee43d"
data_git_msg = """\
commit 4a949ee43da5ce26e1c8d338a1f1cbb370a0b82e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Sat Jul 2 00:49:16 2022 -0400

    [test] Add e2e bare_metal test
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
