import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12234"
version_tuple = (0, 0, 12234)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12234")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12106"
data_version_tuple = (0, 0, 12106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12106")
except ImportError:
    pass
data_git_hash = "ec62501314cc087aa49037eb15c2dc34118d4132"
data_git_describe = "v0.0-12106-gec6250131"
data_git_msg = """\
commit ec62501314cc087aa49037eb15c2dc34118d4132
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed May 18 16:17:46 2022 -0400

    [opentitantool] Fix comment typo
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
