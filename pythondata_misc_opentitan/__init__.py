import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14730"
version_tuple = (0, 0, 14730)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14730")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14588"
data_version_tuple = (0, 0, 14588)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14588")
except ImportError:
    pass
data_git_hash = "7818a4406ec12eaed2aa15f1071a6868ec7a9df1"
data_git_describe = "v0.0-14588-g7818a4406e"
data_git_msg = """\
commit 7818a4406ec12eaed2aa15f1071a6868ec7a9df1
Author: Michał Mazurek <maz@semihalf.com>
Date:   Tue Oct 11 20:06:41 2022 +0200

    [util,tock] Fix invalid TockOS bitfields generation in reggentool.py
    
    Add name sanitizer to enum filed in TockOS register bitfields generator.
    Fix generation of TockOS bitfileds with only one sub-item.
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
