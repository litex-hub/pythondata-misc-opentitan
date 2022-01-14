import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9538"
version_tuple = (0, 0, 9538)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9538")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9416"
data_version_tuple = (0, 0, 9416)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9416")
except ImportError:
    pass
data_git_hash = "10c66e44abff84b940c95d89ceb35d987c1001bb"
data_git_describe = "v0.0-9416-g10c66e44a"
data_git_msg = """\
commit 10c66e44abff84b940c95d89ceb35d987c1001bb
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Jan 11 15:20:03 2022 +0000

    [sw,otbn] Adjust loaders to properly handle OTBN's new bss section.
    
    This change adjusts the OTBN build script to categorize the .bss section
    as .bss rather than .rodata for .rv32embed.o files, which means it is no
    longer guaranteed that DMEM regions are continuous in memory. The
    loaders are then adjusted to handle the two separate sections.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
