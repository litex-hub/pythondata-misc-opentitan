import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11500"
version_tuple = (0, 0, 11500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11374"
data_version_tuple = (0, 0, 11374)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11374")
except ImportError:
    pass
data_git_hash = "5f49e9cabfad06e7fdad5cde65e99d67be3683ce"
data_git_describe = "v0.0-11374-g5f49e9cab"
data_git_msg = """\
commit 5f49e9cabfad06e7fdad5cde65e99d67be3683ce
Author: Weicai Yang <weicai@google.com>
Date:   Fri Apr 8 11:05:13 2022 -0700

    [dv] Add TL error case - write with instr_type = True
    
    Addressed #11902
    Signed-off-by: Weicai Yang <weicai@google.com>

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
