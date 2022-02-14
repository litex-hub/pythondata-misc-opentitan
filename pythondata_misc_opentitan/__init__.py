import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10295"
version_tuple = (0, 0, 10295)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10295")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10169"
data_version_tuple = (0, 0, 10169)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10169")
except ImportError:
    pass
data_git_hash = "a89805ede8763de8f23b585684f540c86a66f39e"
data_git_describe = "v0.0-10169-ga89805ede"
data_git_msg = """\
commit a89805ede8763de8f23b585684f540c86a66f39e
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Feb 11 15:35:49 2022 -0800

    [kmac] Address the D2S review A.Is
    
    - Name changed to CFG_SHADOWED from CONFIG
    - LFSR.REDUN to explicitly say `prim_double_lfsr` not `prim_lfsr`
    - The description of LFSR.REDUN in RTL is revised. LFSR mismatch is
      reported to the alert_handler not FSM
    - CTR.REDUN: `prim_counter` -> `prim_count` / `redundency` ->
      `redundancy`.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
