import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11401"
version_tuple = (0, 0, 11401)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11401")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11275"
data_version_tuple = (0, 0, 11275)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11275")
except ImportError:
    pass
data_git_hash = "ba67a8a11681036fe10bb9f1188dc6e59f738e10"
data_git_describe = "v0.0-11275-gba67a8a11"
data_git_msg = """\
commit ba67a8a11681036fe10bb9f1188dc6e59f738e10
Author: Cindy Liu <hcindyl@google.com>
Date:   Tue Apr 5 11:54:36 2022 -0700

    Update lowrisc_misc-linters to lowRISC/misc-linters@22b6464
    
    Update code from upstream repository https://github.com/lowRISC/misc-
    linters.git to revision 22b64646f079e00866930ed10ee547f81566ac94
    
    * Reformat licence-checker.py to satisfy yapf (Rupert Swarbrick)
    * [licence-checker] Fix vlt checker syntax (Cindy Liu)
    
    Signed-off-by: Cindy Liu <hcindyl@google.com>

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
