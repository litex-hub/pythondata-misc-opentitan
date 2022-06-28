import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12862"
version_tuple = (0, 0, 12862)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12862")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12720"
data_version_tuple = (0, 0, 12720)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12720")
except ImportError:
    pass
data_git_hash = "00185f52cebfc7fad86d1449d79575315c4b7c2a"
data_git_describe = "v0.0-12720-g00185f52ce"
data_git_msg = """\
commit 00185f52cebfc7fad86d1449d79575315c4b7c2a
Author: Weicai Yang <weicai@google.com>
Date:   Mon Jun 27 14:46:56 2022 -0700

    [dv] Fix ping exclusion
    
    Since we enable prim_alert_sender toggle coverage, need to apply ping
    exclusion to this module too.
    
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
