import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10482"
version_tuple = (0, 0, 10482)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10482")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10356"
data_version_tuple = (0, 0, 10356)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10356")
except ImportError:
    pass
data_git_hash = "e5a3f30b286f1d659333165c1c221184a18fbfb1"
data_git_describe = "v0.0-10356-ge5a3f30b2"
data_git_msg = """\
commit e5a3f30b286f1d659333165c1c221184a18fbfb1
Author: Miles Dai <milesdai@google.com>
Date:   Wed Feb 2 17:12:09 2022 +0000

    [mask_rom/e2e_tests] Mask ROM E2E testplan
    
    This commit adds the initial list of testpoints for end-to-end testing
    of the Mask ROM.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
