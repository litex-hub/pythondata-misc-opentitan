import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5058"
version_tuple = (0, 0, 5058)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5058")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4967"
data_version_tuple = (0, 0, 4967)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4967")
except ImportError:
    pass
data_git_hash = "3bb4f0b18142884c5c22223c779bac8878c143a5"
data_git_describe = "v0.0-4967-g3bb4f0b18"
data_git_msg = """\
commit 3bb4f0b18142884c5c22223c779bac8878c143a5
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Feb 19 15:07:00 2021 +0000

    [otbn] Signal multiple errors together
    
    Previously when several errors were observed together OTBN prioritised
    them to set a single error bit. This removes the priortisation so bits
    for all observed errors are set simultaneously.
    
    Fixes #5141
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
