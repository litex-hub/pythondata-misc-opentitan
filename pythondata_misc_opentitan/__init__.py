import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9604"
version_tuple = (0, 0, 9604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9482"
data_version_tuple = (0, 0, 9482)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9482")
except ImportError:
    pass
data_git_hash = "df8b8cd626942a121ea6541caafaad4dbd3f14f9"
data_git_describe = "v0.0-9482-gdf8b8cd62"
data_git_msg = """\
commit df8b8cd626942a121ea6541caafaad4dbd3f14f9
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Jan 11 18:03:15 2022 +0000

    [rom_ctrl,doc] Expand countermeasure list
    
    This is going to be the starting point for both the D2S review and
    also any extra testplan items that go into V2S. Try to explicitly list
    all the extra tricks we're playing.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
