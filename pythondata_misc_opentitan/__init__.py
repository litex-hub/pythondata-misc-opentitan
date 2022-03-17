import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10934"
version_tuple = (0, 0, 10934)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10934")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10808"
data_version_tuple = (0, 0, 10808)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10808")
except ImportError:
    pass
data_git_hash = "4c75bf9687c490f7eebc5d524c7d66a21dafcced"
data_git_describe = "v0.0-10808-g4c75bf968"
data_git_msg = """\
commit 4c75bf9687c490f7eebc5d524c7d66a21dafcced
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Mar 15 17:30:21 2022 -0700

    [dv] Add ROM-only chip-level test example
    
    A few chip-level tests (e.g., `chip_sw_flash_init`) must run and
    complete entirely in the ROM stage. This means that the conventional
    mechanism for running chip-level tests at the flash (ROM_EXT) stage is
    not suitable for such tests.
    
    This commit overcomes this by adding a mechanism to build a chip-level
    test to be run in ROM using the meson build system. (Conveniently, the
    `opentitan_functest` rule already provides such a mechanism using the
    `test_in_rom` rule option.) Additionally, this commit updates the DV
    testbench to skip loading of a flash image (either via bootstrap or via
    the backdoor mem util mechanism) if no such flash image is provided at
    runtime. Lastly, an example ROM-stage chip-level test is added to verify
    the correctness of the added infrastructure, and to provide a reference
    point for future chip-level test development.
    
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
