import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14429"
version_tuple = (0, 0, 14429)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14429")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14287"
data_version_tuple = (0, 0, 14287)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14287")
except ImportError:
    pass
data_git_hash = "ee392e02414608c7ccacb2fde6f132a728614267"
data_git_describe = "v0.0-14287-gee392e0241"
data_git_msg = """\
commit ee392e02414608c7ccacb2fde6f132a728614267
Author: Timothy Trippel <ttrippel@google.com>
Date:   Sat Sep 24 06:10:02 2022 +0000

    [bazel] rollback #15119
    
    Rolling back #15119, as this did not fix bazel airgapped builds.
    
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
