import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10175"
version_tuple = (0, 0, 10175)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10175")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10051"
data_version_tuple = (0, 0, 10051)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10051")
except ImportError:
    pass
data_git_hash = "563312c8cabd3f135c58df639634e741e241d638"
data_git_describe = "v0.0-10051-g563312c8c"
data_git_msg = """\
commit 563312c8cabd3f135c58df639634e741e241d638
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Feb 2 15:10:28 2022 -0800

    [sw/ottf] Rename test_rom_ext to ottf_start
    
    Previously the boot sequence for chip level tests looked like:
    
    chip reset --> test_rom --> test_rom_ext --> ottf --> test_main()
    
    In the above sequence the `test_rom_ext` was really just an ASM file
    that performed initializations prior to jumping to the OTTF `main()`.
    However, as we refactor the OTTF to enable running chip-level tests at
    various boot stages (e.g., ROM_EXT and BL0, see #10498), it makes more
    sense to model the combined OTTF and test bundle as its own boot stage
    that can be run in inplace of the ROM_EXT or BL0.
    
    Therefore, this commit renames/consolidates the test_rom_ext into a
    component of the OTTF, called the `ottf_start`. The `ottf_start` is kept
    as a separate static library from the `ottf` to enable running tests
    that do not use the OTTF, i.e. the crt_test (which tests the
    functionality of the `ottf_start` library), and the "Hello World"
    example programs. However, when test images are built, both the
    `ottf_start` and `ottf` are linked with the test library itself, to
    create one cohesive "test boot stage".
    
    The new boot sequence for a test will look like:
    
    chip reset --> test_rom --> ottf --> test_main(),
    
    where OTTF = (ottf_start --> OTTF).
    
    This partially addresses a task in #10498.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
