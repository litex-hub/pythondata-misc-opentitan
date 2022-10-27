import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14978"
version_tuple = (0, 0, 14978)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14978")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14836"
data_version_tuple = (0, 0, 14836)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14836")
except ImportError:
    pass
data_git_hash = "f58cda5ab437a3a2a5b60427c2963f97e7336c18"
data_git_describe = "v0.0-14836-gf58cda5ab4"
data_git_msg = """\
commit f58cda5ab437a3a2a5b60427c2963f97e7336c18
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jun 13 22:41:48 2022 +0200

    [aes] Rework SecAllowForcingMasks parameter
    
    Previously, if enabled this parameter would allow forcing the output of
    the masking PRNG to 0 requiring 160 MUXs. This was okay for FPGA but not
    for ES.
    
    With this commit, the design is changed as follows:
    - Upon enabling the parameter and setting the FORCE_MASKS bit in the
      auxiliary control register (protected by both a shadow register and
      REGWEN register), the PRNG is no longer advanced. It's output is kept
      constant.
    - To switch off the masking, EDN/CSRNG have further to be configured to
      produce a special seed. Only with this seed and the PRNG output being
      held constant, the masking is off.
    
    This is related to lowRISC/OpenTitan#14240.
    
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
