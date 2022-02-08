import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10121"
version_tuple = (0, 0, 10121)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10121")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9997"
data_version_tuple = (0, 0, 9997)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9997")
except ImportError:
    pass
data_git_hash = "72f98d6f87cb58bbcaf96f28d2b99b6c4333a6ee"
data_git_describe = "v0.0-9997-g72f98d6f8"
data_git_msg = """\
commit 72f98d6f87cb58bbcaf96f28d2b99b6c4333a6ee
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Feb 4 11:59:22 2022 +0100

    [aes/doc] Update documentation based on D2S review
    
    In particular, this commit documents:
    - the use of multi-rail control logic,
    - the need for a system-supplied reset in case of FI detection,
    - worst-case entropy consumption rates
    - the re-use of partial, intermediate results for remasking among
      DOM S-Boxes.
    
    This is related to lowRISC/OpenTitan#10422.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
