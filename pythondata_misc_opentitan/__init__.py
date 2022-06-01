import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12440"
version_tuple = (0, 0, 12440)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12440")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12298"
data_version_tuple = (0, 0, 12298)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12298")
except ImportError:
    pass
data_git_hash = "8fce9b07d969c484eac2af6e73587935c41ae3e9"
data_git_describe = "v0.0-12298-g8fce9b07d"
data_git_msg = """\
commit 8fce9b07d969c484eac2af6e73587935c41ae3e9
Author: Drew Macrae <drewmacrae@google.com>
Date:   Tue May 31 22:07:17 2022 -0400

    [bazel] rename hw/ip/otp_ctrl/data:rma_image_verilator to img_rma
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
