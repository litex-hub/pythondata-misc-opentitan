import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5106"
version_tuple = (0, 0, 5106)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5106")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5015"
data_version_tuple = (0, 0, 5015)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5015")
except ImportError:
    pass
data_git_hash = "f52bf205c43ecc7fc9f27830e810e187498c2400"
data_git_describe = "v0.0-5015-gf52bf205c"
data_git_msg = """\
commit f52bf205c43ecc7fc9f27830e810e187498c2400
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Feb 15 19:17:11 2021 +0000

    [otbn] Enable ECDSA P-256 sign/verify test in CI
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
