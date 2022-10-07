import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14611"
version_tuple = (0, 0, 14611)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14611")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14469"
data_version_tuple = (0, 0, 14469)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14469")
except ImportError:
    pass
data_git_hash = "f70583d912cf1f343fbf5f67dc80f44fab557a49"
data_git_describe = "v0.0-14469-gf70583d912"
data_git_msg = """\
commit f70583d912cf1f343fbf5f67dc80f44fab557a49
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 5 21:18:49 2022 -0700

    [bazel] update rules_rust to use current tip of tree
    
    This updates the rules_rust Bazel depedency to use the upstream rules.
    These now work in an airgapped environment.
    
    Additionally, this has the unfortunate side-effect of temporarily
    disabling rust-analyzer. To use rust-analyzer requires setting the
    `include_rustc_srcs` parameter to `true` in the
    `rust_toolchain_repository` repository rule invocation. However, setting
    this to true, while using the nighly rust toolchains breaks airgapped
    bazel builds because upstream `rules_rust` does not maintain a list of
    known SHA256s for the nightly srcs. Therefore the download of the src
    code that is triggered by setting `include_rustc_srcs` to `true` is not
    cached.
    
    This issue will need to be addressed in upstream `rules_rust`, and will
    be handled externally.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
