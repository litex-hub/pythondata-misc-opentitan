import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15281"
version_tuple = (0, 0, 15281)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15281")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15139"
data_version_tuple = (0, 0, 15139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15139")
except ImportError:
    pass
data_git_hash = "72211c306ccacc11da7f4f2059c291690abcf9de"
data_git_describe = "v0.0-15139-g72211c306c"
data_git_msg = """\
commit 72211c306ccacc11da7f4f2059c291690abcf9de
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Sat Nov 5 09:24:02 2022 -0700

    [chip dv] Coverage exclusions
    
    - Updated pinmux / padctrl el file with more exclusions due to tie offs.
    - Added exclusion for entropy source extended health test interface (unconnected)
    - Added exclusion for ROM ctrl -> kmac app interface (tied off data and strobe)
    - Updated chip coverage collection criteria to only dump port toggle coverage
      on ibex_top instance (skip port toggles on its submodules)
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
