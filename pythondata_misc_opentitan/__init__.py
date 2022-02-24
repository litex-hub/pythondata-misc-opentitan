import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10505"
version_tuple = (0, 0, 10505)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10505")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10379"
data_version_tuple = (0, 0, 10379)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10379")
except ImportError:
    pass
data_git_hash = "df0596a177a1c5c6f249db7858a054ff343cf7f2"
data_git_describe = "v0.0-10379-gdf0596a17"
data_git_msg = """\
commit df0596a177a1c5c6f249db7858a054ff343cf7f2
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Feb 17 16:45:16 2022 -0800

    [sram_ctrl] Align behavior of global and local escalation
    
    Before, global escalation caused the sram_ctrl to block transactions on
    top of other defenses (like scrapping the key, blanking return data).
    Local escalation on the other hand did not cause the sram_ctrl to block
    transactions.
    
    This patch aligns the behavior of both escalations (block transactions),
    since both are fatal conditions.
    
    See #10909 for context.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
