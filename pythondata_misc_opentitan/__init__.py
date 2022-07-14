import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13092"
version_tuple = (0, 0, 13092)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13092")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12950"
data_version_tuple = (0, 0, 12950)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12950")
except ImportError:
    pass
data_git_hash = "98dd7941bb7364c53ee93747745540440294f7ad"
data_git_describe = "v0.0-12950-g98dd7941bb"
data_git_msg = """\
commit 98dd7941bb7364c53ee93747745540440294f7ad
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Jul 13 16:39:55 2022 -0700

    [dif/entropy_src] add DIF to retrieve alert test failure counts
    
    This adds a DIF and corresponding unit tests to retrieve alert test
    failure counts.
    
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
