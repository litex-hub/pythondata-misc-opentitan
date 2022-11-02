import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15142"
version_tuple = (0, 0, 15142)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15142")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15000"
data_version_tuple = (0, 0, 15000)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15000")
except ImportError:
    pass
data_git_hash = "a5deee053c8c8c95396b0ebd7b4bfefac018ec11"
data_git_describe = "v0.0-15000-ga5deee053c"
data_git_msg = """\
commit a5deee053c8c8c95396b0ebd7b4bfefac018ec11
Author: Jacob Levy <jacob.levy@nuvoton.com>
Date:   Tue Oct 25 13:10:58 2022 +0300

    [ast] Add 'plusargs' for regulators power-up acceleration
    
    Signed-off-by: Jacob Levy <jacob.levy@nuvoton.com>

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
