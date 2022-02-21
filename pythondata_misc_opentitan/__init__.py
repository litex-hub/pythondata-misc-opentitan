import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10460"
version_tuple = (0, 0, 10460)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10460")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10334"
data_version_tuple = (0, 0, 10334)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10334")
except ImportError:
    pass
data_git_hash = "01b2cace65124bcbd9fc63acc44eb686c67ff1b3"
data_git_describe = "v0.0-10334-g01b2cace6"
data_git_msg = """\
commit 01b2cace65124bcbd9fc63acc44eb686c67ff1b3
Author: Luís Marques <luismarques@lowrisc.org>
Date:   Thu Feb 10 21:48:11 2022 +0000

    Update toolchain to release 20220210-1 with bitmanip support
    
    This release updates the meson cross files to make the toolchains more
    easily configurable. The tool versions for the bitmanip variant are:
    
    - Binutils 2.35
    - GCC: 10.2.0
    - Clang/LLVM: 13.0.1
    - GDB 11.1
    
    - Binutils: `7c9dd840fbb6a1171a51feb08afb859288615137`
      (riscv-binutils-2.35-rvb) with Pirmin's bitmanip 1.00+0.93 PR patch
      (https://github.com/riscv-collab/riscv-binutils-gdb/pull/267).
    - GCC: `73055647d33c0b63a3125c372019d1dac0f8ac34` (RISC-V bitmanip fork,
      branch riscv-gcc-10.2.0-rvb, commit 73055647d33 from 2021-07-09)
    - Clang/LLVM: 13.0.1
    - GDB 11.1
    
    Signed-off-by: Luís Marques <luismarques@lowrisc.org>

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
