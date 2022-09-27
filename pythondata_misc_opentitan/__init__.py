import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14451"
version_tuple = (0, 0, 14451)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14451")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14309"
data_version_tuple = (0, 0, 14309)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14309")
except ImportError:
    pass
data_git_hash = "75e9c17354d9c01aa257b2e2996c1b635c5a003e"
data_git_describe = "v0.0-14309-g75e9c17354"
data_git_msg = """\
commit 75e9c17354d9c01aa257b2e2996c1b635c5a003e
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Sep 23 14:20:14 2022 -0700

    [rom/e2e] add smoke testpoint and map unmapped test in DV
    
    The simplest of ROM E2E tests, that checked if ROM could successfully
    boot and execute a test (that simple returned `true`) via the OTTF using
    default test infrastructure configurations, was running in DV but was
    not mapped to a test point in the ROM E2E testplan. This adds a
    testpoint for said test and fixes #14679.
    
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
