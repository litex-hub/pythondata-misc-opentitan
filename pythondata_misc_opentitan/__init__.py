import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5635"
version_tuple = (0, 0, 5635)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5635")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5540"
data_version_tuple = (0, 0, 5540)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5540")
except ImportError:
    pass
data_git_hash = "be2128572d11a544d589cd752e35e58efa312951"
data_git_describe = "v0.0-5540-gbe2128572"
data_git_msg = """\
commit be2128572d11a544d589cd752e35e58efa312951
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 30 08:43:11 2021 +0100

    [reggen] Fix name for "u_reg" backdoor in RAL code
    
    The generated RAL code needs to know where to find the generated
    register in the design. Before this patch, we had it hardcoded as
    "u_reg" but that isn't going to work if there are multiple register
    blocks in the design(!).
    
    Here, we use the same naming convention as the rest of the reggen
    code: if a device interface has an explicit name, "foo", we assume
    things relating to the interface get a "_foo" suffix.
    
    Also fix the name of the one example in the tree (in rom_ctrl.sv) to
    match this convention.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
