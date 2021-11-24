import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8860"
version_tuple = (0, 0, 8860)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8860")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8748"
data_version_tuple = (0, 0, 8748)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8748")
except ImportError:
    pass
data_git_hash = "399af406069a3123f13380368bef66db0f17a62a"
data_git_describe = "v0.0-8748-g399af4060"
data_git_msg = """\
commit 399af406069a3123f13380368bef66db0f17a62a
Author: Drew Macrae <drewmacrae@google.com>
Date:   Mon Nov 1 18:15:09 2021 +0000

    [bazel] Rules to build the boot-rom.
    
    * Adding resources to stamp the bootrom
    * Fulfilling and tweaking boot-rom dependencies for bazel
     * scramble_image.py
     * rom_chip_info.py
      * take version input as a file not a command-line arg
    * added autogen for hw/ip/rv_core_ibex/data
    * Added a rule to autogen chip_info
    * Added a rule to build ibex_peri.c in sw/device/lib
    * added a shell script to list details of workspace for a boot-rom stamp
    
    Tested:
    ```
    build/lowrisc_dv_chip_verilator_sim_0.1/sim-verilator/Vchip_sim_tb
    --meminit=rom,bazel-out/k8-fastbuild-ST-b8775c98f59c/bin/sw/device/boot_rom/boot_rom_verilator.scr.40.vmem
    --meminit=flash,bazel-out/k8-fastbuild-ST-b8775c98f59c/bin/sw/device/examples/hello_world/hello_world_verilator.elf
    --meminit=otp,build-bin/sw/device/otp_img/otp_img_sim_verilator.vmem
    ```
    outputs:
    ```
    I00001 boot_rom.c:70] Boot ROM initialisation has completed, jump into
    flash!
    ```
    to uart0.log
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
