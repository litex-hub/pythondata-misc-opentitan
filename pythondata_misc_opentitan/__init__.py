import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10458"
version_tuple = (0, 0, 10458)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10458")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10332"
data_version_tuple = (0, 0, 10332)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10332")
except ImportError:
    pass
data_git_hash = "a1d15ef5e8954da1cdc8dc6171a8afb5747eb925"
data_git_describe = "v0.0-10332-ga1d15ef5e"
data_git_msg = """\
commit a1d15ef5e8954da1cdc8dc6171a8afb5747eb925
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Feb 21 09:18:25 2022 +0100

    [csrng] Update AscentLint waiver
    
    CSRNG uses an unmasked AES cipher core intentionally. We can thus waive
    all the lint errors related to non-default values for the SecMasking
    and SecSBoxImpl parameters.
    
    This is related to lowRISC/OpenTitan#10844.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
