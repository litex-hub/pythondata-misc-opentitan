import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11303"
version_tuple = (0, 0, 11303)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11303")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11177"
data_version_tuple = (0, 0, 11177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11177")
except ImportError:
    pass
data_git_hash = "20e09e06a1b4d021d5210b691451b4b03dd8b173"
data_git_describe = "v0.0-11177-g20e09e06a"
data_git_msg = """\
commit 20e09e06a1b4d021d5210b691451b4b03dd8b173
Author: Jacob Levy <jacob.levy@nuvoton.com>
Date:   Tue Mar 15 17:21:56 2022 +0200

    [ast] Fix CDC and DFT issues
    
    Signed-off-by: Jacob Levy <jacob.levy@nuvoton.com>

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
