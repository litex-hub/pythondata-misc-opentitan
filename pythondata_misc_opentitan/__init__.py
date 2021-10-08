import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8181"
version_tuple = (0, 0, 8181)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8181")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8069"
data_version_tuple = (0, 0, 8069)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8069")
except ImportError:
    pass
data_git_hash = "49bbe18f00acd0d96fb074469ae294180ecdf364"
data_git_describe = "v0.0-8069-g49bbe18f0"
data_git_msg = """\
commit 49bbe18f00acd0d96fb074469ae294180ecdf364
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Oct 7 00:17:46 2021 +0000

    [dif/kmac] Integrate autogen'd DIF artifacts into src tree.
    
    This commit partially addresses #8142. Specifically it:
    1. deprecates existing (manually implemented) **KMAC**
       specific DIF return codes and toggle types,
    2. integrates the auto-generated **KMAC** DIFs into meson build
       targets,
    3. refactors all existing source code to make use of the new shared DIF
       types and error codes, and
    4. embeds the MMIO base address for the IP directly into the IP's DIF
       context handle struct (i.e., `dif_kmac_t`).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
