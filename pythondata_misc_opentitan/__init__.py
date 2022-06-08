import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12566"
version_tuple = (0, 0, 12566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12424"
data_version_tuple = (0, 0, 12424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12424")
except ImportError:
    pass
data_git_hash = "fc26c5a4767291b1c1ac797d5d808eee8c576b9c"
data_git_describe = "v0.0-12424-gfc26c5a47"
data_git_msg = """\
commit fc26c5a4767291b1c1ac797d5d808eee8c576b9c
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jun 7 19:33:37 2022 -0700

    Revert "chore(ci): Skip FPGA , SW test for CDC changes"
    
    This reverts commit 2f48edc13fec8fd3787988100028f2ee107e766d.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
