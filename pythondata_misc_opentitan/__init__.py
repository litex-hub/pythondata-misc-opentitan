import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14185"
version_tuple = (0, 0, 14185)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14185")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14043"
data_version_tuple = (0, 0, 14043)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14043")
except ImportError:
    pass
data_git_hash = "d93ed33baf9cd3227b1f78acfd55222746f4383e"
data_git_describe = "v0.0-14043-gd93ed33baf"
data_git_msg = """\
commit d93ed33baf9cd3227b1f78acfd55222746f4383e
Author: Dan Petrisko <petrisko@cs.washington.edu>
Date:   Tue Sep 13 01:25:16 2022 -0700

    Review fixes
    
    Signed-off-by: Dan Petrisko <petrisko@cs.washington.edu>

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
