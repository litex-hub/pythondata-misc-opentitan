import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10098"
version_tuple = (0, 0, 10098)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10098")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9974"
data_version_tuple = (0, 0, 9974)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9974")
except ImportError:
    pass
data_git_hash = "feaca732a51129d7c598749bb35813cbe61f88fc"
data_git_describe = "v0.0-9974-gfeaca732a"
data_git_msg = """\
commit feaca732a51129d7c598749bb35813cbe61f88fc
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Feb 3 16:04:17 2022 +0000

    [bazel] Solving little warnings in the SW
    
    //sw/device/silicon_creator/lib:verilator_boot_data_functest is flaky
    with a long timeout so I've adjusted it to eternal to make it repeatable
    and to prevent running it when we're under time pressure
    
    The entropy_smoketest and the verilator_watchdog_functest are flaky with a
    default timeout so I've increased them to long (900s)
    
    I ran `bazel run //:buildifier_fix so it will be cleaner when run on
    other systems and commits.
    
    Also addressing the following warnings that appear during a SW build:
    
    sw/device/lib/dif/dif_kmac_unittest.cc:115:23: warning: comparison of
    integer expressions of different signedness: 'int' and 'const size_t'
    {aka 'const long unsigned int'} [-Wsign-compare]
      115 |     for (int i = 0; i < size; ++i) {
          |                     ~~^~~~~~
    
    sw/device/lib/dif/dif_kmac_unittest.cc:161:21: warning:
    comparison of integer expressions of different signedness: 'int'
    and 'long unsigned int' [-Wsign-compare]
      161 |   for (int i = 0; i < sizeof(uint32_t); i++) {
          |                   ~~^~~~~~~~~~~~~~~~~~
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
