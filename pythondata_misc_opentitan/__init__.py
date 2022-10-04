import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14543"
version_tuple = (0, 0, 14543)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14543")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14401"
data_version_tuple = (0, 0, 14401)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14401")
except ImportError:
    pass
data_git_hash = "7aee16bd0c2cc7543a3ec719894830b8d88befc6"
data_git_describe = "v0.0-14401-g7aee16bd0c"
data_git_msg = """\
commit 7aee16bd0c2cc7543a3ec719894830b8d88befc6
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Aug 31 10:46:22 2022 -0700

    [entropy_src/rtl] Cleanup timing enable network
    
    As discussed in PR #14660 there are many places where enable-clearing
    RNG data or masking internal control signals can cause verification
    challenges. This is a primary motivation for keeping delayed copies of
    the enable signals, to apply delayed enable signals at the appropriate
    points in the pipeline.
    
    Such fine-tooth timing management of the enable/disable signals is not
    good for maintainability.  This commit aims to simplify the network of
    enable signals in the entropy_src core, while fixing a number of
    regression failures.
    
    Data pathways that had previously been blocked the instance the module
    was disabled have now been allowed to flow, letting data propagate until
    it stalls at the SHA3 conditioner or gets dropped at the bypass FIFO.
    
    At the same time, this commit simplifies and documents the timing of the
    module enable signals, both the `es_enable` level signal as well as the
    `module_enable_pulse`.
    
    The module_enable_pulse is now one cycle long, and generated from an
    explicit flop. (As opposed to using a prim_mubi4_sync),  AsyncOn=1. The
    es_enable level signal starts in the cycle right after the
    module_enable_pulse, but falls immediately when the module_enable
    register is set to MuBi4False.
    
    Since both the enable pulse, and the enable level signal are derived
    from the same Mubi field, they are fanned-out in MuBi representation.
    
    All of the prim_mubi_sync's now use AsyncOn(0).
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
