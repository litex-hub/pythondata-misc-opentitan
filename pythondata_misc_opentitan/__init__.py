import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12735"
version_tuple = (0, 0, 12735)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12735")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12593"
data_version_tuple = (0, 0, 12593)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12593")
except ImportError:
    pass
data_git_hash = "307059b0448b81cca10b290f7f0d03d1399f3182"
data_git_describe = "v0.0-12593-g307059b04"
data_git_msg = """\
commit 307059b0448b81cca10b290f7f0d03d1399f3182
Author: Weicai Yang <weicai@google.com>
Date:   Fri Jun 10 12:47:23 2022 -0700

    [dv] Remove workaround in the common mem test
    
    Removed workaround for #5262
    Signed-off-by: Weicai Yang <weicai@google.com>

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
