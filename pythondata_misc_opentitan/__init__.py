import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12915"
version_tuple = (0, 0, 12915)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12915")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12773"
data_version_tuple = (0, 0, 12773)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12773")
except ImportError:
    pass
data_git_hash = "2c6196533f33b493e2d56b8a61ebfa620d8503da"
data_git_describe = "v0.0-12773-g2c6196533f"
data_git_msg = """\
commit 2c6196533f33b493e2d56b8a61ebfa620d8503da
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue May 31 10:35:23 2022 +0100

    [test, entropy_src] Add `chip_sw_entropy_src_ast_rng_req` test
    
    Fixes lowrisc/opentitan#13231
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
