import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10343"
version_tuple = (0, 0, 10343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10217"
data_version_tuple = (0, 0, 10217)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10217")
except ImportError:
    pass
data_git_hash = "966ca78eef4b08728ba8b818566ea0ca35a18c45"
data_git_describe = "v0.0-10217-g966ca78ee"
data_git_msg = """\
commit 966ca78eef4b08728ba8b818566ea0ca35a18c45
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Feb 9 10:16:47 2022 +0000

    [rom_ctrl, dv] Added kmac_err_chk testcase
    
    kmac_err_chk testcase added to the testplan along with changes necessary
    to run the test.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
