import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10773"
version_tuple = (0, 0, 10773)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10773")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10647"
data_version_tuple = (0, 0, 10647)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10647")
except ImportError:
    pass
data_git_hash = "ff1944cca2954721cebfa8e9f90087f955a308a9"
data_git_describe = "v0.0-10647-gff1944cca"
data_git_msg = """\
commit ff1944cca2954721cebfa8e9f90087f955a308a9
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Mar 8 12:43:38 2022 +0000

    [sw,crypto] Bazel target for non-mask-ROM RSA-3072 entrypoint.
    
    Now that OTBN binaries can have shared dependencies, use that new
    ability to create an additional target for the RSA-3072 executable that
    is not specialized to mask ROM.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
