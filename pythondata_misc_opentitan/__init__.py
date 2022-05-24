import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12300"
version_tuple = (0, 0, 12300)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12300")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12172"
data_version_tuple = (0, 0, 12172)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12172")
except ImportError:
    pass
data_git_hash = "657c9114c4d73249ff42e0a6f2b003937bac99c1"
data_git_describe = "v0.0-12172-g657c9114c"
data_git_msg = """\
commit 657c9114c4d73249ff42e0a6f2b003937bac99c1
Author: Madhuri Patel <madhuri.patel@ensilica.com>
Date:   Wed May 4 15:46:22 2022 +0100

    [pattgen,dv] Updated pattgen DV checklist
    
    Signed-off-by: Madhuri Patel <madhuri.patel@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
