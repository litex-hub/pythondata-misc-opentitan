import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8698"
version_tuple = (0, 0, 8698)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8698")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8586"
data_version_tuple = (0, 0, 8586)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8586")
except ImportError:
    pass
data_git_hash = "c2775af586fa74121a218d5c68620dcedf1041eb"
data_git_describe = "v0.0-8586-gc2775af58"
data_git_msg = """\
commit c2775af586fa74121a218d5c68620dcedf1041eb
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Nov 10 11:25:51 2021 +0000

    [util] Move some generic parsing code to util
    
    This is used in the OTBN code to convert dictionaries parsed from YAML
    or hjson into proper objects. This patch moves the code to a new
    util/serialize directory and teaches the OTBN code that was using it
    how to find the new version.
    
    The idea is that this might be useful for tightening up parsing in
    e.g. reggen and topgen and will hopefully also be useful for future
    tooling.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
