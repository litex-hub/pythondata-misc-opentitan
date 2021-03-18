import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5460"
version_tuple = (0, 0, 5460)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5460")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5365"
data_version_tuple = (0, 0, 5365)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5365")
except ImportError:
    pass
data_git_hash = "7fa33424764f4f6b8baeb84c5440db6200b0fc16"
data_git_describe = "v0.0-5365-g7fa334247"
data_git_msg = """\
commit 7fa33424764f4f6b8baeb84c5440db6200b0fc16
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Tue Mar 9 12:11:59 2021 +0000

    [test, systemtest] Add MaskROM + ROM_EXT apps selfchecking
    
    This change allows to run both set of tests in CI (boot_rom and Silicon
    Creator). At the moment only a single smoke test (UART) has been added
    to run via Silicon Creator code.
    
    Rationale:
    The main idea is to add some intial MaskROM + ROM_EXT testing without
    disturbing the existing test set-up.
    
    The new added test has passed, checked locally:
    ```
    cd $REPO_TOP
    mkdir build-bin/hw
    
    ln -sf \
    `pwd`/build/lowrisc_systems_top_earlgrey_verilator_0.1/sim-verilator \
    build-bin/hw/top_earlgrey
    
    pytest test/systemtest/earlgrey/test_sim_verilator.py
    ```
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
