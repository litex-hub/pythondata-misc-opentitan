import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9542"
version_tuple = (0, 0, 9542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9420"
data_version_tuple = (0, 0, 9420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9420")
except ImportError:
    pass
data_git_hash = "7dbbbd5410f3aecf120d5d0ec1cbb3b3fd508feb"
data_git_describe = "v0.0-9420-g7dbbbd541"
data_git_msg = """\
commit 7dbbbd5410f3aecf120d5d0ec1cbb3b3fd508feb
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Jan 10 20:28:34 2022 -0800

    [hmac_smoketest] change endianness of expectation
    
    https://github.com/lowRISC/opentitan/pull/9553 has swapped the
    endianness bit to correct it's behavior so the smoke test for the hmac
    needs to have a corrected expectation to pass.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
