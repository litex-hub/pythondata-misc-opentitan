import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5231"
version_tuple = (0, 0, 5231)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5231")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5140"
data_version_tuple = (0, 0, 5140)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5140")
except ImportError:
    pass
data_git_hash = "8a1726fb81612e4abdcc447170eced896c07b9dc"
data_git_describe = "v0.0-5140-g8a1726fb8"
data_git_msg = """\
commit 8a1726fb81612e4abdcc447170eced896c07b9dc
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 3 18:48:23 2021 -0800

    [top] Expand rom to 40b for slightly improved security properties
    
    - Now all Rom nibbles will be fed through the 4-bit sbox, even if
      only 1 round of permutation is done for scrambling
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
