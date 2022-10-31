import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15054"
version_tuple = (0, 0, 15054)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15054")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14912"
data_version_tuple = (0, 0, 14912)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14912")
except ImportError:
    pass
data_git_hash = "999afeda7cc6f4ac00380b37610f53b80c7de304"
data_git_describe = "v0.0-14912-g999afeda7c"
data_git_msg = """\
commit 999afeda7cc6f4ac00380b37610f53b80c7de304
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Fri Oct 14 02:46:45 2022 -0700

    added assertions for  sec_cm_data_reg_local_esc tests
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
