import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12270"
version_tuple = (0, 0, 12270)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12270")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12142"
data_version_tuple = (0, 0, 12142)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12142")
except ImportError:
    pass
data_git_hash = "2a6e9f0277edfdfd8c612c267d37fa0a74e253da"
data_git_describe = "v0.0-12142-g2a6e9f027"
data_git_msg = """\
commit 2a6e9f0277edfdfd8c612c267d37fa0a74e253da
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri May 20 13:08:12 2022 -0400

    [sw/silicon_creator] Relax the default case in bootstrap_handle_program()
    
    We don't expect any other commands since the switch statement covers all
    commands that are handled by SW. However, since we can potentially
    get a 0x0 opcode due to glitches on SPI or strap lines. See #11871.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
