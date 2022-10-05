import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14555"
version_tuple = (0, 0, 14555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14413"
data_version_tuple = (0, 0, 14413)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14413")
except ImportError:
    pass
data_git_hash = "c26f6dc94de1a1428bf068b532396d7e49b5f8a2"
data_git_describe = "v0.0-14413-gc26f6dc94d"
data_git_msg = """\
commit c26f6dc94de1a1428bf068b532396d7e49b5f8a2
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Oct 3 22:20:48 2022 -0700

    [dv,tests] add example concurrency test to DV smoke regression
    
    This addes the example concurrency test to the smoke regression that is
    run in private CI.
    
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
