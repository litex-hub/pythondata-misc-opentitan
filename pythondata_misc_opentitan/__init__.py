import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12999"
version_tuple = (0, 0, 12999)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12999")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12857"
data_version_tuple = (0, 0, 12857)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12857")
except ImportError:
    pass
data_git_hash = "1529c7e02b9bfa10bc30115ca88b1caef4117b70"
data_git_describe = "v0.0-12857-g1529c7e02b"
data_git_msg = """\
commit 1529c7e02b9bfa10bc30115ca88b1caef4117b70
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Jun 24 22:33:05 2022 -0400

    [bazel] Update googletest to release-1.11.0
    
    This commit updates googletest to release-1.11.0 instead of
    the latest release available (1.12.0) because that release has an
    undocumented dependency to @com_googlesource_code_re2 which breaks our
    builds.
    
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
