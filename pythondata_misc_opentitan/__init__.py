import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13305"
version_tuple = (0, 0, 13305)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13305")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13163"
data_version_tuple = (0, 0, 13163)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13163")
except ImportError:
    pass
data_git_hash = "51bbfc42375d721bea21728f88f49de5f3952f63"
data_git_describe = "v0.0-13163-g51bbfc4237"
data_git_msg = """\
commit 51bbfc42375d721bea21728f88f49de5f3952f63
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jul 25 13:09:19 2022 +0200

    [kmac/doc] Clarify purpose of entropy mode configuration values
    
    The idle_mode should really only be used for the very initial ROM_CTRL
    phase. After that software should swtich to either sw_mode or edn_mode
    if the entropy complex is available and importantly also set
    entropy_ready.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
