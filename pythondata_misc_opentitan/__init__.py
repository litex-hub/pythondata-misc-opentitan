import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9735"
version_tuple = (0, 0, 9735)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9735")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9613"
data_version_tuple = (0, 0, 9613)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9613")
except ImportError:
    pass
data_git_hash = "bc4274a6c61dc642785e7f3f82b6c13a358aa5b4"
data_git_describe = "v0.0-9613-gbc4274a6c"
data_git_msg = """\
commit bc4274a6c61dc642785e7f3f82b6c13a358aa5b4
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jan 12 19:30:33 2022 -0800

    [bazel] Add bazel to CI and containers
    
    bazel and gcc-9 is added to azure
    bazel is added to Docker
    ran buildifier
    
    Updated instructions to ask for at least gcc8 the behavior of which is
    already depended on by source in this repo.
    
    skip verilator in bazel builds and tests in CI
    skip targets that depend on verilator.
    add a target so bazel can link it properly in sigverify_dynamic_functest
    
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
