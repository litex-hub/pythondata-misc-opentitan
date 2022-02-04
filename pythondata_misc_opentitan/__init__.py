import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10076"
version_tuple = (0, 0, 10076)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10076")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9952"
data_version_tuple = (0, 0, 9952)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9952")
except ImportError:
    pass
data_git_hash = "e1e90cdc36b1b4003926212f04ea54eb62ad3044"
data_git_describe = "v0.0-9952-ge1e90cdc3"
data_git_msg = """\
commit e1e90cdc36b1b4003926212f04ea54eb62ad3044
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Feb 4 10:01:32 2022 +0100

    [aes] Update sideload key on second write to the shadowed ctrl reg only
    
    Updating the sideload key on every write to the shadow register can
    trigger PRNG reseed operations in the middle of a control register
    update complicating software and DV. For this reason, this commit
    forwards the phase of the shadow register to the main controller to
    only trigger the sideload key update on the second write.
    
    This is related to lowRISC/OpenTitan#10518.
    
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
