import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15319"
version_tuple = (0, 0, 15319)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15319")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15177"
data_version_tuple = (0, 0, 15177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15177")
except ImportError:
    pass
data_git_hash = "a39d3ca93b55e7ae41b77034355692fc9b7aed93"
data_git_describe = "v0.0-15177-ga39d3ca93b"
data_git_msg = """\
commit a39d3ca93b55e7ae41b77034355692fc9b7aed93
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Nov 7 14:09:27 2022 -0800

    [dv,test] add coremark test suite to DV
    
    This commit both:
    1. fixes a runtime error with the coremark test suite that occurred
       because not enough test iterations were run, and
    2. fixes the coremark test's DV configuration.
    
    This fixes #14330.
    
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
