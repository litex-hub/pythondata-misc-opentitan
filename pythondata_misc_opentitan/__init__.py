import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14342"
version_tuple = (0, 0, 14342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14200"
data_version_tuple = (0, 0, 14200)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14200")
except ImportError:
    pass
data_git_hash = "b465af6cff561d6636708c9905dee644f42b5fb4"
data_git_describe = "v0.0-14200-gb465af6cff"
data_git_msg = """\
commit b465af6cff561d6636708c9905dee644f42b5fb4
Author: Guillermo Maturana <maturana@google.com>
Date:   Mon Sep 19 11:57:24 2022 -0700

    [rtl/tlul] Fix typo in tlul_cmd_intg_gen.sv
    
    Also, it is much better to use SV a ":" module_identifier with an
    endmodule, since the compiler checks the identifier matches the module
    name. This is also a good practice for other constructs, like tasks,
    functions, interfaces, packages, classes, etc.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
