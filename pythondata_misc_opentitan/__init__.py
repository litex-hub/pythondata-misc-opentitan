import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14879"
version_tuple = (0, 0, 14879)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14879")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14737"
data_version_tuple = (0, 0, 14737)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14737")
except ImportError:
    pass
data_git_hash = "0f7b76f809315d42c6240cec6e72598b1c2efbdb"
data_git_describe = "v0.0-14737-g0f7b76f809"
data_git_msg = """\
commit 0f7b76f809315d42c6240cec6e72598b1c2efbdb
Author: Michał Mazurek <maz@semihalf.com>
Date:   Mon Oct 17 17:21:38 2022 +0200

    [utils,gpio] Add new hjson key 'auto_split' as hint for regtool
    
    Introduces a new optional key 'auto_split' to serve as a hint
    for register map generator script. Adds support up to 'auto_split'
    in the TockOS register map generator.
    
    If the bitfield or signal has key 'auto_split' set to value
    true generator will split this filed to multiple one-bit fields.
    The name of each generated bitfiled will consist of the
    original bitfield name and an offset. If the parameter is set to false,
    the current behavior of the regtool is not replaced. The default value of the
    new key is set to false.
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
