import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9679"
version_tuple = (0, 0, 9679)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9679")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9557"
data_version_tuple = (0, 0, 9557)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9557")
except ImportError:
    pass
data_git_hash = "001fe330a800777c3a4c13657ac817f5cc5881fa"
data_git_describe = "v0.0-9557-g001fe330a"
data_git_msg = """\
commit 001fe330a800777c3a4c13657ac817f5cc5881fa
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Jan 18 08:30:46 2022 -0800

    [ entropy_src, dv ] Require all seeds to pass at least one round of health checks
    
    The DUT does not allow any data to exit if the most recent health checks have failed.
    This commit updates the scoreboard to note this.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
