import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13027"
version_tuple = (0, 0, 13027)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13027")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12885"
data_version_tuple = (0, 0, 12885)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12885")
except ImportError:
    pass
data_git_hash = "a8e96a0213571207bea750f0e691e8d1521fe4c4"
data_git_describe = "v0.0-12885-ga8e96a0213"
data_git_msg = """\
commit a8e96a0213571207bea750f0e691e8d1521fe4c4
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jul 8 15:14:28 2022 -0700

    [util/dv] Fix sec_cm auto-gen in IP template file
    
    This PR fixes issue #13560 regarding auto-generated ip_template file
    cannot override sec_cm_testplan issue.
    
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
