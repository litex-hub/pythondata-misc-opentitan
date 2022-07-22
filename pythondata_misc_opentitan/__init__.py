import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13251"
version_tuple = (0, 0, 13251)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13251")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13109"
data_version_tuple = (0, 0, 13109)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13109")
except ImportError:
    pass
data_git_hash = "0d212ce0e837443a695626ef94916f75b857a8ef"
data_git_describe = "v0.0-13109-g0d212ce0e8"
data_git_msg = """\
commit 0d212ce0e837443a695626ef94916f75b857a8ef
Author: Dan McArdle <dmcardle@google.com>
Date:   Wed Jul 20 13:12:16 2022 -0400

    [bazel] Add --config=asan and --config=ubsan
    
    These new config flags are intended to be applied to cc_test() targets
    that run on the host machine. For example, the following runs a test
    binary with ASan enabled:
    
      $ ./bazelisk.sh test --config=asan \
        //sw/device/lib/base:status_unittest
    
    Caveat 1: ASan is not implemented for riscv32.
    
      $ ./bazelisk.sh build \
        --platforms=@bazel_embedded//platforms:opentitan_rv32imc \
        --config=asan //sw/device/lib/base:status
      ...
      clang-13: error: unsupported option '-fsanitize=address' for target 'riscv32-unknown-unknown-elf'
      ...
    
    Caveat 2: UBSan is platform-independent, but the linker portion of
    --config=ubsan (-fsanitize=undefined) will not be picked up by custom
    linker scripts.
    
      * This works because :status does not have a custom linker script:
        $ ./bazelisk.sh build \
          --platforms=@bazel_embedded//platforms:opentitan_rv32imc \
          --config=ubsan //sw/device/lib/base:status
    
      * This fails with a linker error:
        $ ./bazelisk.sh test \
          --platforms=@bazel_embedded//platforms:opentitan_rv32imc \
          --config=ubsan //sw/device/lib/testing/test_rom:test_rom
        ...
        /proc/self/cwd/sw/device/silicon_creator/mask_rom/bootstrap.c:320: undefined reference to `__ubsan_handle_builtin_unreachable'
        ...
    
    Issue #13754
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
