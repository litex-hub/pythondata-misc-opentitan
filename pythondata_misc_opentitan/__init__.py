import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14364"
version_tuple = (0, 0, 14364)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14364")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14222"
data_version_tuple = (0, 0, 14222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14222")
except ImportError:
    pass
data_git_hash = "ccb6d24460fe0aec20ba6b8e9e2c0ec0847bde03"
data_git_describe = "v0.0-14222-gccb6d24460"
data_git_msg = """\
commit ccb6d24460fe0aec20ba6b8e9e2c0ec0847bde03
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Sep 21 14:44:02 2022 -0700

    [top/dv] Test triage fix
    
    ensure the test sends enough bytes to trigger the rx watermark
    
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
