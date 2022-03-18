import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10965"
version_tuple = (0, 0, 10965)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10965")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10839"
data_version_tuple = (0, 0, 10839)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10839")
except ImportError:
    pass
data_git_hash = "3fe9fdd8b9b3e18c616e7e400155ba7d48040abb"
data_git_describe = "v0.0-10839-g3fe9fdd8b"
data_git_msg = """\
commit 3fe9fdd8b9b3e18c616e7e400155ba7d48040abb
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Mar 17 14:37:31 2022 -0700

    [chip dv] Fix AST cfg initialization - part 3
    
    - Add knob `do_creator_sw_cfg_ast_cfg` to control whether the AST init
      is done.
    - Change `creator_sw_cfg_ast_cfg_data` to reflect the full set of values
      programmed, including the last REGAL register. This simplifies the
      logic a bit.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
