import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15030"
version_tuple = (0, 0, 15030)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15030")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14888"
data_version_tuple = (0, 0, 14888)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14888")
except ImportError:
    pass
data_git_hash = "da1c2ed8171934c90d44a3b6f56e2c19b06a268d"
data_git_describe = "v0.0-14888-gda1c2ed817"
data_git_msg = """\
commit da1c2ed8171934c90d44a3b6f56e2c19b06a268d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 28 12:24:57 2022 -0700

    [dv/edn] Fix nightly regression failure
    
    This PR fixes nightly regression failure in intr_pin comparison.
    Scb compares intr pin value with intr_state read out value at the
    read_data_phase time, but intr_pin might change at that time.
    
    So a better solution is to store the intr_pin at read_addr_phase, and compare
    the read results later in read_data_phase time.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
