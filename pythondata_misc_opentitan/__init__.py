import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14336"
version_tuple = (0, 0, 14336)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14336")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14194"
data_version_tuple = (0, 0, 14194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14194")
except ImportError:
    pass
data_git_hash = "614df919a602a105be4ff0c105204c05a7cb72ee"
data_git_describe = "v0.0-14194-g614df919a6"
data_git_msg = """\
commit 614df919a602a105be4ff0c105204c05a7cb72ee
Author: Weicai Yang <weicai@google.com>
Date:   Tue Sep 20 15:47:23 2022 -0700

    [chip, dv] Fix chip_tap_straps failures
    
    Fixed typo on the variable and use CASE_EQ to compare as signals could be unknown
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
