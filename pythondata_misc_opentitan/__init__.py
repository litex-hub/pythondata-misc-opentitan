import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12228"
version_tuple = (0, 0, 12228)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12228")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12100"
data_version_tuple = (0, 0, 12100)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12100")
except ImportError:
    pass
data_git_hash = "f770f3ff2349dbd917a2b032b02d2b8485145952"
data_git_describe = "v0.0-12100-gf770f3ff2"
data_git_msg = """\
commit f770f3ff2349dbd917a2b032b02d2b8485145952
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed May 18 10:45:34 2022 -0700

    [sw/base] fix documentation comments in bitfield.h
    
    This addresses some outstanding issues with #12625.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
