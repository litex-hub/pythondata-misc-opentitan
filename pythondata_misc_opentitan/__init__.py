import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5287"
version_tuple = (0, 0, 5287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5192"
data_version_tuple = (0, 0, 5192)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5192")
except ImportError:
    pass
data_git_hash = "b5871b73f4bfa1371901f600b582d77110719440"
data_git_describe = "v0.0-5192-gb5871b73f"
data_git_msg = """\
commit b5871b73f4bfa1371901f600b582d77110719440
Author: Jacob Levy <jacob.levy@opentitan.org>
Date:   Mon Mar 8 21:18:08 2021 +0200

    [AST] AscentLint & Spyglass fixes
    
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
