import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11423"
version_tuple = (0, 0, 11423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11297"
data_version_tuple = (0, 0, 11297)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11297")
except ImportError:
    pass
data_git_hash = "d8b2ed5accf591796a58e0a428ae9670e74d5646"
data_git_describe = "v0.0-11297-gd8b2ed5ac"
data_git_msg = """\
commit d8b2ed5accf591796a58e0a428ae9670e74d5646
Author: Weicai Yang <weicai@google.com>
Date:   Wed Apr 6 14:31:12 2022 -0700

    [flash, dv] Fix CI failures
    
    Due to merging of these 2 PR - #11823 and #11770
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
