import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9718"
version_tuple = (0, 0, 9718)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9718")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9596"
data_version_tuple = (0, 0, 9596)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9596")
except ImportError:
    pass
data_git_hash = "0262e24d61f6019199f47c50d34ae8e7aa0acf20"
data_git_describe = "v0.0-9596-g0262e24d6"
data_git_msg = """\
commit 0262e24d61f6019199f47c50d34ae8e7aa0acf20
Author: Drew Macrae <drewmacrae@google.com>
Date:   Sun Jan 23 19:35:14 2022 -0800

    [bazel] fixup dependency in mask_rom_epmp_test
    
    didn't commit and push the version of the fix I tested and worked on
    for #10280. This commit should actually work to build the
    mask_rom_epmp_test.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
