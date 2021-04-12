import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5819"
version_tuple = (0, 0, 5819)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5819")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5724"
data_version_tuple = (0, 0, 5724)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5724")
except ImportError:
    pass
data_git_hash = "8317b037bc142ac95e4bf3ecfdfafffb7f64ef8c"
data_git_describe = "v0.0-5724-g8317b037b"
data_git_msg = """\
commit 8317b037bc142ac95e4bf3ecfdfafffb7f64ef8c
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Apr 9 14:59:35 2021 +0100

    Update lowrisc_ibex to lowRISC/ibex@25cd6600
    
    Update code from upstream repository
    https://github.com/lowRISC/ibex.git to revision
    25cd6600c64e6eec4c3f5ee20237b53e4d5a3a52
    
    * [dv] Don't kill regression on sim error (Greg Chadwick)
    * [rtl] Add dual core lockstep option (Tom Roberts)
    * [rtl] Add a new top level plus wiring (Tom Roberts)
    * [rtl/icache] Move various parameters into the pkg (Tom Roberts)
    * [rtl] Add SVA to ensure valid_i in compressed decoder is known
      (Pirmin Vogel)
    * Update google_riscv-dv to google/riscv-dv@59dcd8c (Rupert Swarbrick)
    * [util] Document required VCS version (Rupert Swarbrick)
    * [util] Manually "vendor" latest check_tool_requirements.py (Rupert
      Swarbrick)
    * Fix initialisation in ibex_icache_env_cfg.sv (Rupert Swarbrick)
    * Update lowrisc_ip to lowRISC/opentitan@f29a0f7a7 (Rupert Swarbrick)
    * Avoid encumbered name in ibex_icache_testplan.hjson (Rupert
      Swarbrick)
    * [dv] Remove semicolon (Philipp Wagner)
    * [dv] Fix name of ELF file in report (Philipp Wagner)
    * [dv] Fix riscv_nested_interrupt_test (Greg Chadwick)
    * [dv] Fix riscv_irq_in_debug_mode_test (Greg Chadwick)
    * [dv] Allow full IRQ randomisation (Greg Chadwick)
    * [dv] Small core_ibex_test_lib refactor (Greg Chadwick)
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
