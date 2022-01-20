import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9650"
version_tuple = (0, 0, 9650)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9650")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9528"
data_version_tuple = (0, 0, 9528)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9528")
except ImportError:
    pass
data_git_hash = "2e5e1c3222109f34264b6aea7aa1bb2e19baddf9"
data_git_describe = "v0.0-9528-g2e5e1c322"
data_git_msg = """\
commit 2e5e1c3222109f34264b6aea7aa1bb2e19baddf9
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jan 10 12:28:18 2022 +0100

    [aes] Move to D2
    
    All D2 items for AES have been done. Implementation and verification
    of countermeasures have been moved to D2S and V2S stages, respectively.
    Thus, it's time to move AES into D2.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
