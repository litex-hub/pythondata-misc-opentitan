import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13197"
version_tuple = (0, 0, 13197)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13197")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13055"
data_version_tuple = (0, 0, 13055)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13055")
except ImportError:
    pass
data_git_hash = "ca7ed9cf6b733a425ab5333763e9a5fd518d89e8"
data_git_describe = "v0.0-13055-gca7ed9cf6b"
data_git_msg = """\
commit ca7ed9cf6b733a425ab5333763e9a5fd518d89e8
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Jul 19 10:13:54 2022 -0700

    [dvsim] Make email.html filename more descriptive
    
    This commit makes 2 changes to the generated reports:
    - Remove `latest` symlink in the reports area
    - Make email.html filename more descriptive, i.e. reflective of
      what hjson cfg was run, the tool flow and the tool.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
