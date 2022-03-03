import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10667"
version_tuple = (0, 0, 10667)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10667")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10541"
data_version_tuple = (0, 0, 10541)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10541")
except ImportError:
    pass
data_git_hash = "e3a7c579dc0d4785156ea3999e84004cc6c4ecf2"
data_git_describe = "v0.0-10541-ge3a7c579d"
data_git_msg = """\
commit e3a7c579dc0d4785156ea3999e84004cc6c4ecf2
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Feb 17 17:30:47 2022 -0800

    [bazel] Restructure `opentitan_binary` and `opentitan_functest` macros
    
    Verilator simulations can take as input either a scrambled VMEM file or
    an ELF file to load the simulated flash memory with. However, the
    existing signing tool, can only sign BIN files, and BIN files can only
    be converted to VMEM files (since ELF section header info is lost).
    Therefore, in order to run Verilator simulations with signed flash
    images, for mask ROM testing, the bazel `opentitan_binary` macro must
    be able to convert singed BIN files into scrambled VMEM files.
    
    Currently, the `opentitan_binary` macro is used to generate both ROM and
    flash images for simulations, since the simulated ROM takes as input a
    scrambled VMEM file, that can be generated from an ELF file (so the
    same macro could generate ELFs for either ROM or flash, and if the image
    was destined for ROM, it could just be processed further).
    
    Unfortunately, the scrambled VMEM format used for ROM, is different from
    that used for flash (i.e., 32 vs. 64 bit words), and, using the
    same bazel macro (i.e., `opentitan_binary`) to generate two different
    scrambled VMEM files (one for ROM and one for flash) adds too much
    complexity to the macro.
    
    Therefore, this commit, brakes the original `opentitan_binary` macro
    intro three macros, to simplify the implementation of each, while
    maximizing code reuse. These include:
    
    1. `opentitan_binary`: a macro used to generate ".elf", ".bin", and
       ".dis" files for RV32I targets,
    2. `opentitan_rom_binary`: a macro that invokes `opentitan_binary`
       under the hood, and then translates the resulting ".elf" into a
       scrambled 32-bit VMEM file (required for ROM), and
    3. `opentitan_flash_binary`: a macro that invokes `opentitan_binary`
       under the hood, and then (optionally) signs, and translates the
       resulting ".bin" files into scrambled 64-bit VMEM files (required
       for flash).
    
    This fixes #10876, and enables running `opentitan_functest`s with mask
    ROM (and test ROM) on both Verilator and CW310 hardware targets.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
