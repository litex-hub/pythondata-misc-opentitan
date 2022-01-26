import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9815"
version_tuple = (0, 0, 9815)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9815")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9693"
data_version_tuple = (0, 0, 9693)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9693")
except ImportError:
    pass
data_git_hash = "51fde5a9830ab1501b01d953c7651c63727a546d"
data_git_describe = "v0.0-9693-g51fde5a98"
data_git_msg = """\
commit 51fde5a9830ab1501b01d953c7651c63727a546d
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Jan 7 14:46:56 2022 -0800

    [entropy_src/rtl] Modify enable registers
    
    This PR makes two broad changes to the entropy_src enable registers:
    
    - The conf.enable field has been split into two registers
      - module_enable.module_enable: for overall activation of the IP in
        any context (BOOT_ROM or otherwise)
      - conf.fips_enable: For activation of strict RNG health testing, using
        stricter CC or FIPS grade health-test thresholds (not recommended
        for BOOT_ROM driven operation).
    - For better sequencing control, and error handling capabilities, the
      module_enable has been split out into its own register, with a
      separate write enable control (REGWEN_ME vs. REGWEN).
    
    Note on Software guidelines following this commit:
    
    The appropriate use of these registers depends on whether they are
    set in the BOOT_ROM or in later (mutable) C-code:
    
    - The enable fields should only differ when set by the BOOT ROM, which
      uses a preliminary set of health test thresholds.  Here, the
      MODULE_ENABLE should be set _without_ setting the FIPS_ENABLE field.
      This indicates that the stronger "FIPS" thresholds have not been set,
      and the IP is not configured for reliable entropy generation.
    
    - For all later, DIF-driven software stages we assume that the
      "Module" enable and the "FIPS" enable are always set together,
      after the final stricter health test thresholds have been set.
    
    Fixes #9637.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>
    Co-authored-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
