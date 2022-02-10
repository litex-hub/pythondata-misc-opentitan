import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10211"
version_tuple = (0, 0, 10211)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10211")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10087"
data_version_tuple = (0, 0, 10087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10087")
except ImportError:
    pass
data_git_hash = "cb96560f187f6af9b5461d55eaf18ab3f5515901"
data_git_describe = "v0.0-10087-gcb96560f1"
data_git_msg = """\
commit cb96560f187f6af9b5461d55eaf18ab3f5515901
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Feb 8 15:41:47 2022 -0800

    [sw/ottf] Add manifest to OTTF so mask ROM can (eventually) boot it
    
    This adds a manifest field to any test images that are run via the
    ottf_start.S assembly. This includes any tests that use the OTTF itself
    (e.g., chip-level tests), and tests with a `main()` entrypoint (e.g.,
    "Hello World" example programs).
    
    Note, this just adds the manifest fields to OTTF test binaries, and sets
    the default entry point to `_ottf_start`. It does not place the manifest
    in the correct location such that it can be loaded and verified by the
    mask ROM. That will come in a subsequent commit.
    
    This addresses task in #10498.
    
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
