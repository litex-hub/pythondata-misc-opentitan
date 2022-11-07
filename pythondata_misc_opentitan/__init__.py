import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15265"
version_tuple = (0, 0, 15265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15123"
data_version_tuple = (0, 0, 15123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15123")
except ImportError:
    pass
data_git_hash = "f7b050d242fe469061ebdb23d8ee059172d89879"
data_git_describe = "v0.0-15123-gf7b050d242"
data_git_msg = """\
commit f7b050d242fe469061ebdb23d8ee059172d89879
Author: Miles Dai <milesdai@google.com>
Date:   Wed Nov 2 16:34:05 2022 -0400

    [otp/ast] Enable AST initialization in Bazel-generated OTP images
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
