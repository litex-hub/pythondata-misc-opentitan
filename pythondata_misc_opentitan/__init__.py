import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14260"
version_tuple = (0, 0, 14260)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14260")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14118"
data_version_tuple = (0, 0, 14118)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14118")
except ImportError:
    pass
data_git_hash = "476fd521585a806fcbce21a41e6e5dded2207c4b"
data_git_describe = "v0.0-14118-g476fd52158"
data_git_msg = """\
commit 476fd521585a806fcbce21a41e6e5dded2207c4b
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Sep 15 16:39:47 2022 -0700

    [util/topgen] Update alert lpg generation
    
    - fixes #14954
    
    The alert lpg generation currently uses the clock group, clock domain
    and power domain of a particular clock to uniquely identify lpg groups.
    
    As a result, it lumps all the transactional clocks of the same domains
    into one group.  This behavior however is not correct, as the
    transactional clocks are unique and can be individually gated.
    
    This commit updates the lpg generation to take this into account.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
