import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12960"
version_tuple = (0, 0, 12960)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12960")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12818"
data_version_tuple = (0, 0, 12818)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12818")
except ImportError:
    pass
data_git_hash = "39dca1d60c7a2f7f3a56eea1885511de06281472"
data_git_describe = "v0.0-12818-g39dca1d60c"
data_git_msg = """\
commit 39dca1d60c7a2f7f3a56eea1885511de06281472
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Jul 6 18:42:35 2022 -0700

    [bazel] add SHAs for all rust crates
    
    This adds missing SHAs for all rust crates to enable/fix airgapped builds of
    opentitantool.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
