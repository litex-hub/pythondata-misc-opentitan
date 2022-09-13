import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14152"
version_tuple = (0, 0, 14152)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14152")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14010"
data_version_tuple = (0, 0, 14010)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14010")
except ImportError:
    pass
data_git_hash = "5dbc328dfd71f8be72c3403eee83c22c79deb318"
data_git_describe = "v0.0-14010-g5dbc328dfd"
data_git_msg = """\
commit 5dbc328dfd71f8be72c3403eee83c22c79deb318
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Sep 1 12:26:31 2022 -0400

    [sw/silicon_creator, test] Move shared constants to toplevel_memory.ld.tpl
    
    This commit moves linker constants such as stack size, chip info size,
    etc. to toplevel_memory.ld.tpl. Since the linker script generated from
    this template is included by rom, rom_ext, bare_metal, and ottf linker
    scripts, this change makes it easier to keep all these settings in sync.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
