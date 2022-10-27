// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// xbar_main module generated by `tlgen.py` tool
// all reset signals should be generated from one reset signal to not make any deadlock
//
// Interconnect
// rv_core_ibex.corei
//   -> s1n_27
//     -> sm1_28
//       -> rom_ctrl.rom
//     -> sm1_29
//       -> rv_dm.mem
//     -> sm1_30
//       -> sram_ctrl_main.ram
//     -> sm1_31
//       -> flash_ctrl.mem
// rv_core_ibex.cored
//   -> s1n_32
//     -> sm1_28
//       -> rom_ctrl.rom
//     -> sm1_33
//       -> rom_ctrl.regs
//     -> sm1_29
//       -> rv_dm.mem
//     -> sm1_34
//       -> rv_dm.regs
//     -> sm1_30
//       -> sram_ctrl_main.ram
//     -> sm1_36
//       -> asf_35
//         -> peri
//     -> sm1_38
//       -> asf_37
//         -> spi_host0
//     -> sm1_40
//       -> asf_39
//         -> spi_host1
//     -> sm1_42
//       -> asf_41
//         -> usbdev
//     -> sm1_43
//       -> flash_ctrl.core
//     -> sm1_44
//       -> flash_ctrl.prim
//     -> sm1_31
//       -> flash_ctrl.mem
//     -> sm1_45
//       -> aes
//     -> sm1_46
//       -> entropy_src
//     -> sm1_47
//       -> csrng
//     -> sm1_48
//       -> edn0
//     -> sm1_49
//       -> edn1
//     -> sm1_50
//       -> hmac
//     -> sm1_51
//       -> rv_plic
//     -> sm1_52
//       -> otbn
//     -> sm1_53
//       -> keymgr
//     -> sm1_54
//       -> kmac
//     -> sm1_55
//       -> sram_ctrl_main.regs
//     -> sm1_56
//       -> rv_core_ibex.cfg
// rv_dm.sba
//   -> s1n_57
//     -> sm1_28
//       -> rom_ctrl.rom
//     -> sm1_33
//       -> rom_ctrl.regs
//     -> sm1_29
//       -> rv_dm.mem
//     -> sm1_34
//       -> rv_dm.regs
//     -> sm1_30
//       -> sram_ctrl_main.ram
//     -> sm1_36
//       -> asf_35
//         -> peri
//     -> sm1_38
//       -> asf_37
//         -> spi_host0
//     -> sm1_40
//       -> asf_39
//         -> spi_host1
//     -> sm1_42
//       -> asf_41
//         -> usbdev
//     -> sm1_43
//       -> flash_ctrl.core
//     -> sm1_44
//       -> flash_ctrl.prim
//     -> sm1_31
//       -> flash_ctrl.mem
//     -> sm1_45
//       -> aes
//     -> sm1_46
//       -> entropy_src
//     -> sm1_47
//       -> csrng
//     -> sm1_48
//       -> edn0
//     -> sm1_49
//       -> edn1
//     -> sm1_50
//       -> hmac
//     -> sm1_51
//       -> rv_plic
//     -> sm1_52
//       -> otbn
//     -> sm1_53
//       -> keymgr
//     -> sm1_54
//       -> kmac
//     -> sm1_55
//       -> sram_ctrl_main.regs
//     -> sm1_56
//       -> rv_core_ibex.cfg

module xbar_main (
  input clk_main_i,
  input clk_fixed_i,
  input clk_usb_i,
  input clk_spi_host0_i,
  input clk_spi_host1_i,
  input rst_main_ni,
  input rst_fixed_ni,
  input rst_usb_ni,
  input rst_spi_host0_ni,
  input rst_spi_host1_ni,

  // Host interfaces
  input  tlul_pkg::tl_h2d_t tl_rv_core_ibex__corei_i,
  output tlul_pkg::tl_d2h_t tl_rv_core_ibex__corei_o,
  input  tlul_pkg::tl_h2d_t tl_rv_core_ibex__cored_i,
  output tlul_pkg::tl_d2h_t tl_rv_core_ibex__cored_o,
  input  tlul_pkg::tl_h2d_t tl_rv_dm__sba_i,
  output tlul_pkg::tl_d2h_t tl_rv_dm__sba_o,

  // Device interfaces
  output tlul_pkg::tl_h2d_t tl_rv_dm__regs_o,
  input  tlul_pkg::tl_d2h_t tl_rv_dm__regs_i,
  output tlul_pkg::tl_h2d_t tl_rv_dm__mem_o,
  input  tlul_pkg::tl_d2h_t tl_rv_dm__mem_i,
  output tlul_pkg::tl_h2d_t tl_rom_ctrl__rom_o,
  input  tlul_pkg::tl_d2h_t tl_rom_ctrl__rom_i,
  output tlul_pkg::tl_h2d_t tl_rom_ctrl__regs_o,
  input  tlul_pkg::tl_d2h_t tl_rom_ctrl__regs_i,
  output tlul_pkg::tl_h2d_t tl_peri_o,
  input  tlul_pkg::tl_d2h_t tl_peri_i,
  output tlul_pkg::tl_h2d_t tl_spi_host0_o,
  input  tlul_pkg::tl_d2h_t tl_spi_host0_i,
  output tlul_pkg::tl_h2d_t tl_spi_host1_o,
  input  tlul_pkg::tl_d2h_t tl_spi_host1_i,
  output tlul_pkg::tl_h2d_t tl_usbdev_o,
  input  tlul_pkg::tl_d2h_t tl_usbdev_i,
  output tlul_pkg::tl_h2d_t tl_flash_ctrl__core_o,
  input  tlul_pkg::tl_d2h_t tl_flash_ctrl__core_i,
  output tlul_pkg::tl_h2d_t tl_flash_ctrl__prim_o,
  input  tlul_pkg::tl_d2h_t tl_flash_ctrl__prim_i,
  output tlul_pkg::tl_h2d_t tl_flash_ctrl__mem_o,
  input  tlul_pkg::tl_d2h_t tl_flash_ctrl__mem_i,
  output tlul_pkg::tl_h2d_t tl_hmac_o,
  input  tlul_pkg::tl_d2h_t tl_hmac_i,
  output tlul_pkg::tl_h2d_t tl_kmac_o,
  input  tlul_pkg::tl_d2h_t tl_kmac_i,
  output tlul_pkg::tl_h2d_t tl_aes_o,
  input  tlul_pkg::tl_d2h_t tl_aes_i,
  output tlul_pkg::tl_h2d_t tl_entropy_src_o,
  input  tlul_pkg::tl_d2h_t tl_entropy_src_i,
  output tlul_pkg::tl_h2d_t tl_csrng_o,
  input  tlul_pkg::tl_d2h_t tl_csrng_i,
  output tlul_pkg::tl_h2d_t tl_edn0_o,
  input  tlul_pkg::tl_d2h_t tl_edn0_i,
  output tlul_pkg::tl_h2d_t tl_edn1_o,
  input  tlul_pkg::tl_d2h_t tl_edn1_i,
  output tlul_pkg::tl_h2d_t tl_rv_plic_o,
  input  tlul_pkg::tl_d2h_t tl_rv_plic_i,
  output tlul_pkg::tl_h2d_t tl_otbn_o,
  input  tlul_pkg::tl_d2h_t tl_otbn_i,
  output tlul_pkg::tl_h2d_t tl_keymgr_o,
  input  tlul_pkg::tl_d2h_t tl_keymgr_i,
  output tlul_pkg::tl_h2d_t tl_rv_core_ibex__cfg_o,
  input  tlul_pkg::tl_d2h_t tl_rv_core_ibex__cfg_i,
  output tlul_pkg::tl_h2d_t tl_sram_ctrl_main__regs_o,
  input  tlul_pkg::tl_d2h_t tl_sram_ctrl_main__regs_i,
  output tlul_pkg::tl_h2d_t tl_sram_ctrl_main__ram_o,
  input  tlul_pkg::tl_d2h_t tl_sram_ctrl_main__ram_i,

  input prim_mubi_pkg::mubi4_t scanmode_i
);

  import tlul_pkg::*;
  import tl_main_pkg::*;

  // scanmode_i is currently not used, but provisioned for future use
  // this assignment prevents lint warnings
  logic unused_scanmode;
  assign unused_scanmode = ^scanmode_i;

  tl_h2d_t tl_s1n_27_us_h2d ;
  tl_d2h_t tl_s1n_27_us_d2h ;


  tl_h2d_t tl_s1n_27_ds_h2d [4];
  tl_d2h_t tl_s1n_27_ds_d2h [4];

  // Create steering signal
  logic [2:0] dev_sel_s1n_27;


  tl_h2d_t tl_sm1_28_us_h2d [3];
  tl_d2h_t tl_sm1_28_us_d2h [3];

  tl_h2d_t tl_sm1_28_ds_h2d ;
  tl_d2h_t tl_sm1_28_ds_d2h ;


  tl_h2d_t tl_sm1_29_us_h2d [3];
  tl_d2h_t tl_sm1_29_us_d2h [3];

  tl_h2d_t tl_sm1_29_ds_h2d ;
  tl_d2h_t tl_sm1_29_ds_d2h ;


  tl_h2d_t tl_sm1_30_us_h2d [3];
  tl_d2h_t tl_sm1_30_us_d2h [3];

  tl_h2d_t tl_sm1_30_ds_h2d ;
  tl_d2h_t tl_sm1_30_ds_d2h ;


  tl_h2d_t tl_sm1_31_us_h2d [3];
  tl_d2h_t tl_sm1_31_us_d2h [3];

  tl_h2d_t tl_sm1_31_ds_h2d ;
  tl_d2h_t tl_sm1_31_ds_d2h ;

  tl_h2d_t tl_s1n_32_us_h2d ;
  tl_d2h_t tl_s1n_32_us_d2h ;


  tl_h2d_t tl_s1n_32_ds_h2d [24];
  tl_d2h_t tl_s1n_32_ds_d2h [24];

  // Create steering signal
  logic [4:0] dev_sel_s1n_32;


  tl_h2d_t tl_sm1_33_us_h2d [2];
  tl_d2h_t tl_sm1_33_us_d2h [2];

  tl_h2d_t tl_sm1_33_ds_h2d ;
  tl_d2h_t tl_sm1_33_ds_d2h ;


  tl_h2d_t tl_sm1_34_us_h2d [2];
  tl_d2h_t tl_sm1_34_us_d2h [2];

  tl_h2d_t tl_sm1_34_ds_h2d ;
  tl_d2h_t tl_sm1_34_ds_d2h ;

  tl_h2d_t tl_asf_35_us_h2d ;
  tl_d2h_t tl_asf_35_us_d2h ;
  tl_h2d_t tl_asf_35_ds_h2d ;
  tl_d2h_t tl_asf_35_ds_d2h ;


  tl_h2d_t tl_sm1_36_us_h2d [2];
  tl_d2h_t tl_sm1_36_us_d2h [2];

  tl_h2d_t tl_sm1_36_ds_h2d ;
  tl_d2h_t tl_sm1_36_ds_d2h ;

  tl_h2d_t tl_asf_37_us_h2d ;
  tl_d2h_t tl_asf_37_us_d2h ;
  tl_h2d_t tl_asf_37_ds_h2d ;
  tl_d2h_t tl_asf_37_ds_d2h ;


  tl_h2d_t tl_sm1_38_us_h2d [2];
  tl_d2h_t tl_sm1_38_us_d2h [2];

  tl_h2d_t tl_sm1_38_ds_h2d ;
  tl_d2h_t tl_sm1_38_ds_d2h ;

  tl_h2d_t tl_asf_39_us_h2d ;
  tl_d2h_t tl_asf_39_us_d2h ;
  tl_h2d_t tl_asf_39_ds_h2d ;
  tl_d2h_t tl_asf_39_ds_d2h ;


  tl_h2d_t tl_sm1_40_us_h2d [2];
  tl_d2h_t tl_sm1_40_us_d2h [2];

  tl_h2d_t tl_sm1_40_ds_h2d ;
  tl_d2h_t tl_sm1_40_ds_d2h ;

  tl_h2d_t tl_asf_41_us_h2d ;
  tl_d2h_t tl_asf_41_us_d2h ;
  tl_h2d_t tl_asf_41_ds_h2d ;
  tl_d2h_t tl_asf_41_ds_d2h ;


  tl_h2d_t tl_sm1_42_us_h2d [2];
  tl_d2h_t tl_sm1_42_us_d2h [2];

  tl_h2d_t tl_sm1_42_ds_h2d ;
  tl_d2h_t tl_sm1_42_ds_d2h ;


  tl_h2d_t tl_sm1_43_us_h2d [2];
  tl_d2h_t tl_sm1_43_us_d2h [2];

  tl_h2d_t tl_sm1_43_ds_h2d ;
  tl_d2h_t tl_sm1_43_ds_d2h ;


  tl_h2d_t tl_sm1_44_us_h2d [2];
  tl_d2h_t tl_sm1_44_us_d2h [2];

  tl_h2d_t tl_sm1_44_ds_h2d ;
  tl_d2h_t tl_sm1_44_ds_d2h ;


  tl_h2d_t tl_sm1_45_us_h2d [2];
  tl_d2h_t tl_sm1_45_us_d2h [2];

  tl_h2d_t tl_sm1_45_ds_h2d ;
  tl_d2h_t tl_sm1_45_ds_d2h ;


  tl_h2d_t tl_sm1_46_us_h2d [2];
  tl_d2h_t tl_sm1_46_us_d2h [2];

  tl_h2d_t tl_sm1_46_ds_h2d ;
  tl_d2h_t tl_sm1_46_ds_d2h ;


  tl_h2d_t tl_sm1_47_us_h2d [2];
  tl_d2h_t tl_sm1_47_us_d2h [2];

  tl_h2d_t tl_sm1_47_ds_h2d ;
  tl_d2h_t tl_sm1_47_ds_d2h ;


  tl_h2d_t tl_sm1_48_us_h2d [2];
  tl_d2h_t tl_sm1_48_us_d2h [2];

  tl_h2d_t tl_sm1_48_ds_h2d ;
  tl_d2h_t tl_sm1_48_ds_d2h ;


  tl_h2d_t tl_sm1_49_us_h2d [2];
  tl_d2h_t tl_sm1_49_us_d2h [2];

  tl_h2d_t tl_sm1_49_ds_h2d ;
  tl_d2h_t tl_sm1_49_ds_d2h ;


  tl_h2d_t tl_sm1_50_us_h2d [2];
  tl_d2h_t tl_sm1_50_us_d2h [2];

  tl_h2d_t tl_sm1_50_ds_h2d ;
  tl_d2h_t tl_sm1_50_ds_d2h ;


  tl_h2d_t tl_sm1_51_us_h2d [2];
  tl_d2h_t tl_sm1_51_us_d2h [2];

  tl_h2d_t tl_sm1_51_ds_h2d ;
  tl_d2h_t tl_sm1_51_ds_d2h ;


  tl_h2d_t tl_sm1_52_us_h2d [2];
  tl_d2h_t tl_sm1_52_us_d2h [2];

  tl_h2d_t tl_sm1_52_ds_h2d ;
  tl_d2h_t tl_sm1_52_ds_d2h ;


  tl_h2d_t tl_sm1_53_us_h2d [2];
  tl_d2h_t tl_sm1_53_us_d2h [2];

  tl_h2d_t tl_sm1_53_ds_h2d ;
  tl_d2h_t tl_sm1_53_ds_d2h ;


  tl_h2d_t tl_sm1_54_us_h2d [2];
  tl_d2h_t tl_sm1_54_us_d2h [2];

  tl_h2d_t tl_sm1_54_ds_h2d ;
  tl_d2h_t tl_sm1_54_ds_d2h ;


  tl_h2d_t tl_sm1_55_us_h2d [2];
  tl_d2h_t tl_sm1_55_us_d2h [2];

  tl_h2d_t tl_sm1_55_ds_h2d ;
  tl_d2h_t tl_sm1_55_ds_d2h ;


  tl_h2d_t tl_sm1_56_us_h2d [2];
  tl_d2h_t tl_sm1_56_us_d2h [2];

  tl_h2d_t tl_sm1_56_ds_h2d ;
  tl_d2h_t tl_sm1_56_ds_d2h ;

  tl_h2d_t tl_s1n_57_us_h2d ;
  tl_d2h_t tl_s1n_57_us_d2h ;


  tl_h2d_t tl_s1n_57_ds_h2d [24];
  tl_d2h_t tl_s1n_57_ds_d2h [24];

  // Create steering signal
  logic [4:0] dev_sel_s1n_57;



  assign tl_sm1_28_us_h2d[0] = tl_s1n_27_ds_h2d[0];
  assign tl_s1n_27_ds_d2h[0] = tl_sm1_28_us_d2h[0];

  assign tl_sm1_29_us_h2d[0] = tl_s1n_27_ds_h2d[1];
  assign tl_s1n_27_ds_d2h[1] = tl_sm1_29_us_d2h[0];

  assign tl_sm1_30_us_h2d[0] = tl_s1n_27_ds_h2d[2];
  assign tl_s1n_27_ds_d2h[2] = tl_sm1_30_us_d2h[0];

  assign tl_sm1_31_us_h2d[0] = tl_s1n_27_ds_h2d[3];
  assign tl_s1n_27_ds_d2h[3] = tl_sm1_31_us_d2h[0];

  assign tl_sm1_28_us_h2d[1] = tl_s1n_32_ds_h2d[0];
  assign tl_s1n_32_ds_d2h[0] = tl_sm1_28_us_d2h[1];

  assign tl_sm1_33_us_h2d[0] = tl_s1n_32_ds_h2d[1];
  assign tl_s1n_32_ds_d2h[1] = tl_sm1_33_us_d2h[0];

  assign tl_sm1_29_us_h2d[1] = tl_s1n_32_ds_h2d[2];
  assign tl_s1n_32_ds_d2h[2] = tl_sm1_29_us_d2h[1];

  assign tl_sm1_34_us_h2d[0] = tl_s1n_32_ds_h2d[3];
  assign tl_s1n_32_ds_d2h[3] = tl_sm1_34_us_d2h[0];

  assign tl_sm1_30_us_h2d[1] = tl_s1n_32_ds_h2d[4];
  assign tl_s1n_32_ds_d2h[4] = tl_sm1_30_us_d2h[1];

  assign tl_sm1_36_us_h2d[0] = tl_s1n_32_ds_h2d[5];
  assign tl_s1n_32_ds_d2h[5] = tl_sm1_36_us_d2h[0];

  assign tl_sm1_38_us_h2d[0] = tl_s1n_32_ds_h2d[6];
  assign tl_s1n_32_ds_d2h[6] = tl_sm1_38_us_d2h[0];

  assign tl_sm1_40_us_h2d[0] = tl_s1n_32_ds_h2d[7];
  assign tl_s1n_32_ds_d2h[7] = tl_sm1_40_us_d2h[0];

  assign tl_sm1_42_us_h2d[0] = tl_s1n_32_ds_h2d[8];
  assign tl_s1n_32_ds_d2h[8] = tl_sm1_42_us_d2h[0];

  assign tl_sm1_43_us_h2d[0] = tl_s1n_32_ds_h2d[9];
  assign tl_s1n_32_ds_d2h[9] = tl_sm1_43_us_d2h[0];

  assign tl_sm1_44_us_h2d[0] = tl_s1n_32_ds_h2d[10];
  assign tl_s1n_32_ds_d2h[10] = tl_sm1_44_us_d2h[0];

  assign tl_sm1_31_us_h2d[1] = tl_s1n_32_ds_h2d[11];
  assign tl_s1n_32_ds_d2h[11] = tl_sm1_31_us_d2h[1];

  assign tl_sm1_45_us_h2d[0] = tl_s1n_32_ds_h2d[12];
  assign tl_s1n_32_ds_d2h[12] = tl_sm1_45_us_d2h[0];

  assign tl_sm1_46_us_h2d[0] = tl_s1n_32_ds_h2d[13];
  assign tl_s1n_32_ds_d2h[13] = tl_sm1_46_us_d2h[0];

  assign tl_sm1_47_us_h2d[0] = tl_s1n_32_ds_h2d[14];
  assign tl_s1n_32_ds_d2h[14] = tl_sm1_47_us_d2h[0];

  assign tl_sm1_48_us_h2d[0] = tl_s1n_32_ds_h2d[15];
  assign tl_s1n_32_ds_d2h[15] = tl_sm1_48_us_d2h[0];

  assign tl_sm1_49_us_h2d[0] = tl_s1n_32_ds_h2d[16];
  assign tl_s1n_32_ds_d2h[16] = tl_sm1_49_us_d2h[0];

  assign tl_sm1_50_us_h2d[0] = tl_s1n_32_ds_h2d[17];
  assign tl_s1n_32_ds_d2h[17] = tl_sm1_50_us_d2h[0];

  assign tl_sm1_51_us_h2d[0] = tl_s1n_32_ds_h2d[18];
  assign tl_s1n_32_ds_d2h[18] = tl_sm1_51_us_d2h[0];

  assign tl_sm1_52_us_h2d[0] = tl_s1n_32_ds_h2d[19];
  assign tl_s1n_32_ds_d2h[19] = tl_sm1_52_us_d2h[0];

  assign tl_sm1_53_us_h2d[0] = tl_s1n_32_ds_h2d[20];
  assign tl_s1n_32_ds_d2h[20] = tl_sm1_53_us_d2h[0];

  assign tl_sm1_54_us_h2d[0] = tl_s1n_32_ds_h2d[21];
  assign tl_s1n_32_ds_d2h[21] = tl_sm1_54_us_d2h[0];

  assign tl_sm1_55_us_h2d[0] = tl_s1n_32_ds_h2d[22];
  assign tl_s1n_32_ds_d2h[22] = tl_sm1_55_us_d2h[0];

  assign tl_sm1_56_us_h2d[0] = tl_s1n_32_ds_h2d[23];
  assign tl_s1n_32_ds_d2h[23] = tl_sm1_56_us_d2h[0];

  assign tl_sm1_28_us_h2d[2] = tl_s1n_57_ds_h2d[0];
  assign tl_s1n_57_ds_d2h[0] = tl_sm1_28_us_d2h[2];

  assign tl_sm1_33_us_h2d[1] = tl_s1n_57_ds_h2d[1];
  assign tl_s1n_57_ds_d2h[1] = tl_sm1_33_us_d2h[1];

  assign tl_sm1_29_us_h2d[2] = tl_s1n_57_ds_h2d[2];
  assign tl_s1n_57_ds_d2h[2] = tl_sm1_29_us_d2h[2];

  assign tl_sm1_34_us_h2d[1] = tl_s1n_57_ds_h2d[3];
  assign tl_s1n_57_ds_d2h[3] = tl_sm1_34_us_d2h[1];

  assign tl_sm1_30_us_h2d[2] = tl_s1n_57_ds_h2d[4];
  assign tl_s1n_57_ds_d2h[4] = tl_sm1_30_us_d2h[2];

  assign tl_sm1_36_us_h2d[1] = tl_s1n_57_ds_h2d[5];
  assign tl_s1n_57_ds_d2h[5] = tl_sm1_36_us_d2h[1];

  assign tl_sm1_38_us_h2d[1] = tl_s1n_57_ds_h2d[6];
  assign tl_s1n_57_ds_d2h[6] = tl_sm1_38_us_d2h[1];

  assign tl_sm1_40_us_h2d[1] = tl_s1n_57_ds_h2d[7];
  assign tl_s1n_57_ds_d2h[7] = tl_sm1_40_us_d2h[1];

  assign tl_sm1_42_us_h2d[1] = tl_s1n_57_ds_h2d[8];
  assign tl_s1n_57_ds_d2h[8] = tl_sm1_42_us_d2h[1];

  assign tl_sm1_43_us_h2d[1] = tl_s1n_57_ds_h2d[9];
  assign tl_s1n_57_ds_d2h[9] = tl_sm1_43_us_d2h[1];

  assign tl_sm1_44_us_h2d[1] = tl_s1n_57_ds_h2d[10];
  assign tl_s1n_57_ds_d2h[10] = tl_sm1_44_us_d2h[1];

  assign tl_sm1_31_us_h2d[2] = tl_s1n_57_ds_h2d[11];
  assign tl_s1n_57_ds_d2h[11] = tl_sm1_31_us_d2h[2];

  assign tl_sm1_45_us_h2d[1] = tl_s1n_57_ds_h2d[12];
  assign tl_s1n_57_ds_d2h[12] = tl_sm1_45_us_d2h[1];

  assign tl_sm1_46_us_h2d[1] = tl_s1n_57_ds_h2d[13];
  assign tl_s1n_57_ds_d2h[13] = tl_sm1_46_us_d2h[1];

  assign tl_sm1_47_us_h2d[1] = tl_s1n_57_ds_h2d[14];
  assign tl_s1n_57_ds_d2h[14] = tl_sm1_47_us_d2h[1];

  assign tl_sm1_48_us_h2d[1] = tl_s1n_57_ds_h2d[15];
  assign tl_s1n_57_ds_d2h[15] = tl_sm1_48_us_d2h[1];

  assign tl_sm1_49_us_h2d[1] = tl_s1n_57_ds_h2d[16];
  assign tl_s1n_57_ds_d2h[16] = tl_sm1_49_us_d2h[1];

  assign tl_sm1_50_us_h2d[1] = tl_s1n_57_ds_h2d[17];
  assign tl_s1n_57_ds_d2h[17] = tl_sm1_50_us_d2h[1];

  assign tl_sm1_51_us_h2d[1] = tl_s1n_57_ds_h2d[18];
  assign tl_s1n_57_ds_d2h[18] = tl_sm1_51_us_d2h[1];

  assign tl_sm1_52_us_h2d[1] = tl_s1n_57_ds_h2d[19];
  assign tl_s1n_57_ds_d2h[19] = tl_sm1_52_us_d2h[1];

  assign tl_sm1_53_us_h2d[1] = tl_s1n_57_ds_h2d[20];
  assign tl_s1n_57_ds_d2h[20] = tl_sm1_53_us_d2h[1];

  assign tl_sm1_54_us_h2d[1] = tl_s1n_57_ds_h2d[21];
  assign tl_s1n_57_ds_d2h[21] = tl_sm1_54_us_d2h[1];

  assign tl_sm1_55_us_h2d[1] = tl_s1n_57_ds_h2d[22];
  assign tl_s1n_57_ds_d2h[22] = tl_sm1_55_us_d2h[1];

  assign tl_sm1_56_us_h2d[1] = tl_s1n_57_ds_h2d[23];
  assign tl_s1n_57_ds_d2h[23] = tl_sm1_56_us_d2h[1];

  assign tl_s1n_27_us_h2d = tl_rv_core_ibex__corei_i;
  assign tl_rv_core_ibex__corei_o = tl_s1n_27_us_d2h;

  assign tl_rom_ctrl__rom_o = tl_sm1_28_ds_h2d;
  assign tl_sm1_28_ds_d2h = tl_rom_ctrl__rom_i;

  assign tl_rv_dm__mem_o = tl_sm1_29_ds_h2d;
  assign tl_sm1_29_ds_d2h = tl_rv_dm__mem_i;

  assign tl_sram_ctrl_main__ram_o = tl_sm1_30_ds_h2d;
  assign tl_sm1_30_ds_d2h = tl_sram_ctrl_main__ram_i;

  assign tl_flash_ctrl__mem_o = tl_sm1_31_ds_h2d;
  assign tl_sm1_31_ds_d2h = tl_flash_ctrl__mem_i;

  assign tl_s1n_32_us_h2d = tl_rv_core_ibex__cored_i;
  assign tl_rv_core_ibex__cored_o = tl_s1n_32_us_d2h;

  assign tl_rom_ctrl__regs_o = tl_sm1_33_ds_h2d;
  assign tl_sm1_33_ds_d2h = tl_rom_ctrl__regs_i;

  assign tl_rv_dm__regs_o = tl_sm1_34_ds_h2d;
  assign tl_sm1_34_ds_d2h = tl_rv_dm__regs_i;

  assign tl_peri_o = tl_asf_35_ds_h2d;
  assign tl_asf_35_ds_d2h = tl_peri_i;

  assign tl_asf_35_us_h2d = tl_sm1_36_ds_h2d;
  assign tl_sm1_36_ds_d2h = tl_asf_35_us_d2h;

  assign tl_spi_host0_o = tl_asf_37_ds_h2d;
  assign tl_asf_37_ds_d2h = tl_spi_host0_i;

  assign tl_asf_37_us_h2d = tl_sm1_38_ds_h2d;
  assign tl_sm1_38_ds_d2h = tl_asf_37_us_d2h;

  assign tl_spi_host1_o = tl_asf_39_ds_h2d;
  assign tl_asf_39_ds_d2h = tl_spi_host1_i;

  assign tl_asf_39_us_h2d = tl_sm1_40_ds_h2d;
  assign tl_sm1_40_ds_d2h = tl_asf_39_us_d2h;

  assign tl_usbdev_o = tl_asf_41_ds_h2d;
  assign tl_asf_41_ds_d2h = tl_usbdev_i;

  assign tl_asf_41_us_h2d = tl_sm1_42_ds_h2d;
  assign tl_sm1_42_ds_d2h = tl_asf_41_us_d2h;

  assign tl_flash_ctrl__core_o = tl_sm1_43_ds_h2d;
  assign tl_sm1_43_ds_d2h = tl_flash_ctrl__core_i;

  assign tl_flash_ctrl__prim_o = tl_sm1_44_ds_h2d;
  assign tl_sm1_44_ds_d2h = tl_flash_ctrl__prim_i;

  assign tl_aes_o = tl_sm1_45_ds_h2d;
  assign tl_sm1_45_ds_d2h = tl_aes_i;

  assign tl_entropy_src_o = tl_sm1_46_ds_h2d;
  assign tl_sm1_46_ds_d2h = tl_entropy_src_i;

  assign tl_csrng_o = tl_sm1_47_ds_h2d;
  assign tl_sm1_47_ds_d2h = tl_csrng_i;

  assign tl_edn0_o = tl_sm1_48_ds_h2d;
  assign tl_sm1_48_ds_d2h = tl_edn0_i;

  assign tl_edn1_o = tl_sm1_49_ds_h2d;
  assign tl_sm1_49_ds_d2h = tl_edn1_i;

  assign tl_hmac_o = tl_sm1_50_ds_h2d;
  assign tl_sm1_50_ds_d2h = tl_hmac_i;

  assign tl_rv_plic_o = tl_sm1_51_ds_h2d;
  assign tl_sm1_51_ds_d2h = tl_rv_plic_i;

  assign tl_otbn_o = tl_sm1_52_ds_h2d;
  assign tl_sm1_52_ds_d2h = tl_otbn_i;

  assign tl_keymgr_o = tl_sm1_53_ds_h2d;
  assign tl_sm1_53_ds_d2h = tl_keymgr_i;

  assign tl_kmac_o = tl_sm1_54_ds_h2d;
  assign tl_sm1_54_ds_d2h = tl_kmac_i;

  assign tl_sram_ctrl_main__regs_o = tl_sm1_55_ds_h2d;
  assign tl_sm1_55_ds_d2h = tl_sram_ctrl_main__regs_i;

  assign tl_rv_core_ibex__cfg_o = tl_sm1_56_ds_h2d;
  assign tl_sm1_56_ds_d2h = tl_rv_core_ibex__cfg_i;

  assign tl_s1n_57_us_h2d = tl_rv_dm__sba_i;
  assign tl_rv_dm__sba_o = tl_s1n_57_us_d2h;

  always_comb begin
    // default steering to generate error response if address is not within the range
    dev_sel_s1n_27 = 3'd4;
    if ((tl_s1n_27_us_h2d.a_address &
         ~(ADDR_MASK_ROM_CTRL__ROM)) == ADDR_SPACE_ROM_CTRL__ROM) begin
      dev_sel_s1n_27 = 3'd0;

    end else if ((tl_s1n_27_us_h2d.a_address &
                  ~(ADDR_MASK_RV_DM__MEM)) == ADDR_SPACE_RV_DM__MEM) begin
      dev_sel_s1n_27 = 3'd1;

    end else if ((tl_s1n_27_us_h2d.a_address &
                  ~(ADDR_MASK_SRAM_CTRL_MAIN__RAM)) == ADDR_SPACE_SRAM_CTRL_MAIN__RAM) begin
      dev_sel_s1n_27 = 3'd2;

    end else if ((tl_s1n_27_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__MEM)) == ADDR_SPACE_FLASH_CTRL__MEM) begin
      dev_sel_s1n_27 = 3'd3;
end
  end

  always_comb begin
    // default steering to generate error response if address is not within the range
    dev_sel_s1n_32 = 5'd24;
    if ((tl_s1n_32_us_h2d.a_address &
         ~(ADDR_MASK_ROM_CTRL__ROM)) == ADDR_SPACE_ROM_CTRL__ROM) begin
      dev_sel_s1n_32 = 5'd0;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_ROM_CTRL__REGS)) == ADDR_SPACE_ROM_CTRL__REGS) begin
      dev_sel_s1n_32 = 5'd1;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_RV_DM__MEM)) == ADDR_SPACE_RV_DM__MEM) begin
      dev_sel_s1n_32 = 5'd2;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_RV_DM__REGS)) == ADDR_SPACE_RV_DM__REGS) begin
      dev_sel_s1n_32 = 5'd3;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_SRAM_CTRL_MAIN__RAM)) == ADDR_SPACE_SRAM_CTRL_MAIN__RAM) begin
      dev_sel_s1n_32 = 5'd4;

    end else if (
      ((tl_s1n_32_us_h2d.a_address & ~(ADDR_MASK_PERI[0])) == ADDR_SPACE_PERI[0]) ||
      ((tl_s1n_32_us_h2d.a_address & ~(ADDR_MASK_PERI[1])) == ADDR_SPACE_PERI[1])
    ) begin
      dev_sel_s1n_32 = 5'd5;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_SPI_HOST0)) == ADDR_SPACE_SPI_HOST0) begin
      dev_sel_s1n_32 = 5'd6;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_SPI_HOST1)) == ADDR_SPACE_SPI_HOST1) begin
      dev_sel_s1n_32 = 5'd7;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_USBDEV)) == ADDR_SPACE_USBDEV) begin
      dev_sel_s1n_32 = 5'd8;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__CORE)) == ADDR_SPACE_FLASH_CTRL__CORE) begin
      dev_sel_s1n_32 = 5'd9;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__PRIM)) == ADDR_SPACE_FLASH_CTRL__PRIM) begin
      dev_sel_s1n_32 = 5'd10;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__MEM)) == ADDR_SPACE_FLASH_CTRL__MEM) begin
      dev_sel_s1n_32 = 5'd11;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_AES)) == ADDR_SPACE_AES) begin
      dev_sel_s1n_32 = 5'd12;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_ENTROPY_SRC)) == ADDR_SPACE_ENTROPY_SRC) begin
      dev_sel_s1n_32 = 5'd13;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_CSRNG)) == ADDR_SPACE_CSRNG) begin
      dev_sel_s1n_32 = 5'd14;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_EDN0)) == ADDR_SPACE_EDN0) begin
      dev_sel_s1n_32 = 5'd15;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_EDN1)) == ADDR_SPACE_EDN1) begin
      dev_sel_s1n_32 = 5'd16;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_HMAC)) == ADDR_SPACE_HMAC) begin
      dev_sel_s1n_32 = 5'd17;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_RV_PLIC)) == ADDR_SPACE_RV_PLIC) begin
      dev_sel_s1n_32 = 5'd18;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_OTBN)) == ADDR_SPACE_OTBN) begin
      dev_sel_s1n_32 = 5'd19;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_KEYMGR)) == ADDR_SPACE_KEYMGR) begin
      dev_sel_s1n_32 = 5'd20;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_KMAC)) == ADDR_SPACE_KMAC) begin
      dev_sel_s1n_32 = 5'd21;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_SRAM_CTRL_MAIN__REGS)) == ADDR_SPACE_SRAM_CTRL_MAIN__REGS) begin
      dev_sel_s1n_32 = 5'd22;

    end else if ((tl_s1n_32_us_h2d.a_address &
                  ~(ADDR_MASK_RV_CORE_IBEX__CFG)) == ADDR_SPACE_RV_CORE_IBEX__CFG) begin
      dev_sel_s1n_32 = 5'd23;
end
  end

  always_comb begin
    // default steering to generate error response if address is not within the range
    dev_sel_s1n_57 = 5'd24;
    if ((tl_s1n_57_us_h2d.a_address &
         ~(ADDR_MASK_ROM_CTRL__ROM)) == ADDR_SPACE_ROM_CTRL__ROM) begin
      dev_sel_s1n_57 = 5'd0;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_ROM_CTRL__REGS)) == ADDR_SPACE_ROM_CTRL__REGS) begin
      dev_sel_s1n_57 = 5'd1;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_RV_DM__MEM)) == ADDR_SPACE_RV_DM__MEM) begin
      dev_sel_s1n_57 = 5'd2;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_RV_DM__REGS)) == ADDR_SPACE_RV_DM__REGS) begin
      dev_sel_s1n_57 = 5'd3;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_SRAM_CTRL_MAIN__RAM)) == ADDR_SPACE_SRAM_CTRL_MAIN__RAM) begin
      dev_sel_s1n_57 = 5'd4;

    end else if (
      ((tl_s1n_57_us_h2d.a_address & ~(ADDR_MASK_PERI[0])) == ADDR_SPACE_PERI[0]) ||
      ((tl_s1n_57_us_h2d.a_address & ~(ADDR_MASK_PERI[1])) == ADDR_SPACE_PERI[1])
    ) begin
      dev_sel_s1n_57 = 5'd5;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_SPI_HOST0)) == ADDR_SPACE_SPI_HOST0) begin
      dev_sel_s1n_57 = 5'd6;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_SPI_HOST1)) == ADDR_SPACE_SPI_HOST1) begin
      dev_sel_s1n_57 = 5'd7;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_USBDEV)) == ADDR_SPACE_USBDEV) begin
      dev_sel_s1n_57 = 5'd8;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__CORE)) == ADDR_SPACE_FLASH_CTRL__CORE) begin
      dev_sel_s1n_57 = 5'd9;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__PRIM)) == ADDR_SPACE_FLASH_CTRL__PRIM) begin
      dev_sel_s1n_57 = 5'd10;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_FLASH_CTRL__MEM)) == ADDR_SPACE_FLASH_CTRL__MEM) begin
      dev_sel_s1n_57 = 5'd11;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_AES)) == ADDR_SPACE_AES) begin
      dev_sel_s1n_57 = 5'd12;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_ENTROPY_SRC)) == ADDR_SPACE_ENTROPY_SRC) begin
      dev_sel_s1n_57 = 5'd13;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_CSRNG)) == ADDR_SPACE_CSRNG) begin
      dev_sel_s1n_57 = 5'd14;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_EDN0)) == ADDR_SPACE_EDN0) begin
      dev_sel_s1n_57 = 5'd15;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_EDN1)) == ADDR_SPACE_EDN1) begin
      dev_sel_s1n_57 = 5'd16;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_HMAC)) == ADDR_SPACE_HMAC) begin
      dev_sel_s1n_57 = 5'd17;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_RV_PLIC)) == ADDR_SPACE_RV_PLIC) begin
      dev_sel_s1n_57 = 5'd18;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_OTBN)) == ADDR_SPACE_OTBN) begin
      dev_sel_s1n_57 = 5'd19;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_KEYMGR)) == ADDR_SPACE_KEYMGR) begin
      dev_sel_s1n_57 = 5'd20;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_KMAC)) == ADDR_SPACE_KMAC) begin
      dev_sel_s1n_57 = 5'd21;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_SRAM_CTRL_MAIN__REGS)) == ADDR_SPACE_SRAM_CTRL_MAIN__REGS) begin
      dev_sel_s1n_57 = 5'd22;

    end else if ((tl_s1n_57_us_h2d.a_address &
                  ~(ADDR_MASK_RV_CORE_IBEX__CFG)) == ADDR_SPACE_RV_CORE_IBEX__CFG) begin
      dev_sel_s1n_57 = 5'd23;
end
  end


  // Instantiation phase
  tlul_socket_1n #(
    .HReqDepth (4'h0),
    .HRspDepth (4'h0),
    .DReqDepth (16'h0),
    .DRspDepth (16'h0),
    .N         (4)
  ) u_s1n_27 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_s1n_27_us_h2d),
    .tl_h_o       (tl_s1n_27_us_d2h),
    .tl_d_o       (tl_s1n_27_ds_h2d),
    .tl_d_i       (tl_s1n_27_ds_d2h),
    .dev_select_i (dev_sel_s1n_27)
  );
  tlul_socket_m1 #(
    .HReqDepth (12'h0),
    .HRspDepth (12'h0),
    .DRspPass  (1'b0),
    .M         (3)
  ) u_sm1_28 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_28_us_h2d),
    .tl_h_o       (tl_sm1_28_us_d2h),
    .tl_d_o       (tl_sm1_28_ds_h2d),
    .tl_d_i       (tl_sm1_28_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (12'h0),
    .HRspDepth (12'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (3)
  ) u_sm1_29 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_29_us_h2d),
    .tl_h_o       (tl_sm1_29_us_d2h),
    .tl_d_o       (tl_sm1_29_ds_h2d),
    .tl_d_i       (tl_sm1_29_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (12'h0),
    .HRspDepth (12'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (3)
  ) u_sm1_30 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_30_us_h2d),
    .tl_h_o       (tl_sm1_30_us_d2h),
    .tl_d_o       (tl_sm1_30_ds_h2d),
    .tl_d_i       (tl_sm1_30_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (12'h0),
    .HRspDepth (12'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (3)
  ) u_sm1_31 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_31_us_h2d),
    .tl_h_o       (tl_sm1_31_us_d2h),
    .tl_d_o       (tl_sm1_31_ds_h2d),
    .tl_d_i       (tl_sm1_31_ds_d2h)
  );
  tlul_socket_1n #(
    .HReqDepth (4'h0),
    .HRspDepth (4'h0),
    .DReqDepth (96'h0),
    .DRspDepth (96'h0),
    .N         (24)
  ) u_s1n_32 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_s1n_32_us_h2d),
    .tl_h_o       (tl_s1n_32_us_d2h),
    .tl_d_o       (tl_s1n_32_ds_h2d),
    .tl_d_i       (tl_s1n_32_ds_d2h),
    .dev_select_i (dev_sel_s1n_32)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_33 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_33_us_h2d),
    .tl_h_o       (tl_sm1_33_us_d2h),
    .tl_d_o       (tl_sm1_33_ds_h2d),
    .tl_d_i       (tl_sm1_33_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_34 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_34_us_h2d),
    .tl_h_o       (tl_sm1_34_us_d2h),
    .tl_d_o       (tl_sm1_34_ds_h2d),
    .tl_d_i       (tl_sm1_34_ds_d2h)
  );
  tlul_fifo_async #(
    .ReqDepth        (1),
    .RspDepth        (1)
  ) u_asf_35 (
    .clk_h_i      (clk_main_i),
    .rst_h_ni     (rst_main_ni),
    .clk_d_i      (clk_fixed_i),
    .rst_d_ni     (rst_fixed_ni),
    .tl_h_i       (tl_asf_35_us_h2d),
    .tl_h_o       (tl_asf_35_us_d2h),
    .tl_d_o       (tl_asf_35_ds_h2d),
    .tl_d_i       (tl_asf_35_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_36 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_36_us_h2d),
    .tl_h_o       (tl_sm1_36_us_d2h),
    .tl_d_o       (tl_sm1_36_ds_h2d),
    .tl_d_i       (tl_sm1_36_ds_d2h)
  );
  tlul_fifo_async #(
    .ReqDepth        (1),
    .RspDepth        (1)
  ) u_asf_37 (
    .clk_h_i      (clk_main_i),
    .rst_h_ni     (rst_main_ni),
    .clk_d_i      (clk_spi_host0_i),
    .rst_d_ni     (rst_spi_host0_ni),
    .tl_h_i       (tl_asf_37_us_h2d),
    .tl_h_o       (tl_asf_37_us_d2h),
    .tl_d_o       (tl_asf_37_ds_h2d),
    .tl_d_i       (tl_asf_37_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_38 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_38_us_h2d),
    .tl_h_o       (tl_sm1_38_us_d2h),
    .tl_d_o       (tl_sm1_38_ds_h2d),
    .tl_d_i       (tl_sm1_38_ds_d2h)
  );
  tlul_fifo_async #(
    .ReqDepth        (1),
    .RspDepth        (1)
  ) u_asf_39 (
    .clk_h_i      (clk_main_i),
    .rst_h_ni     (rst_main_ni),
    .clk_d_i      (clk_spi_host1_i),
    .rst_d_ni     (rst_spi_host1_ni),
    .tl_h_i       (tl_asf_39_us_h2d),
    .tl_h_o       (tl_asf_39_us_d2h),
    .tl_d_o       (tl_asf_39_ds_h2d),
    .tl_d_i       (tl_asf_39_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_40 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_40_us_h2d),
    .tl_h_o       (tl_sm1_40_us_d2h),
    .tl_d_o       (tl_sm1_40_ds_h2d),
    .tl_d_i       (tl_sm1_40_ds_d2h)
  );
  tlul_fifo_async #(
    .ReqDepth        (1),
    .RspDepth        (1)
  ) u_asf_41 (
    .clk_h_i      (clk_main_i),
    .rst_h_ni     (rst_main_ni),
    .clk_d_i      (clk_usb_i),
    .rst_d_ni     (rst_usb_ni),
    .tl_h_i       (tl_asf_41_us_h2d),
    .tl_h_o       (tl_asf_41_us_d2h),
    .tl_d_o       (tl_asf_41_ds_h2d),
    .tl_d_i       (tl_asf_41_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_42 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_42_us_h2d),
    .tl_h_o       (tl_sm1_42_us_d2h),
    .tl_d_o       (tl_sm1_42_ds_h2d),
    .tl_d_i       (tl_sm1_42_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_43 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_43_us_h2d),
    .tl_h_o       (tl_sm1_43_us_d2h),
    .tl_d_o       (tl_sm1_43_ds_h2d),
    .tl_d_i       (tl_sm1_43_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_44 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_44_us_h2d),
    .tl_h_o       (tl_sm1_44_us_d2h),
    .tl_d_o       (tl_sm1_44_ds_h2d),
    .tl_d_i       (tl_sm1_44_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_45 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_45_us_h2d),
    .tl_h_o       (tl_sm1_45_us_d2h),
    .tl_d_o       (tl_sm1_45_ds_h2d),
    .tl_d_i       (tl_sm1_45_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_46 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_46_us_h2d),
    .tl_h_o       (tl_sm1_46_us_d2h),
    .tl_d_o       (tl_sm1_46_ds_h2d),
    .tl_d_i       (tl_sm1_46_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_47 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_47_us_h2d),
    .tl_h_o       (tl_sm1_47_us_d2h),
    .tl_d_o       (tl_sm1_47_ds_h2d),
    .tl_d_i       (tl_sm1_47_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_48 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_48_us_h2d),
    .tl_h_o       (tl_sm1_48_us_d2h),
    .tl_d_o       (tl_sm1_48_ds_h2d),
    .tl_d_i       (tl_sm1_48_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_49 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_49_us_h2d),
    .tl_h_o       (tl_sm1_49_us_d2h),
    .tl_d_o       (tl_sm1_49_ds_h2d),
    .tl_d_i       (tl_sm1_49_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_50 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_50_us_h2d),
    .tl_h_o       (tl_sm1_50_us_d2h),
    .tl_d_o       (tl_sm1_50_ds_h2d),
    .tl_d_i       (tl_sm1_50_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_51 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_51_us_h2d),
    .tl_h_o       (tl_sm1_51_us_d2h),
    .tl_d_o       (tl_sm1_51_ds_h2d),
    .tl_d_i       (tl_sm1_51_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_52 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_52_us_h2d),
    .tl_h_o       (tl_sm1_52_us_d2h),
    .tl_d_o       (tl_sm1_52_ds_h2d),
    .tl_d_i       (tl_sm1_52_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_53 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_53_us_h2d),
    .tl_h_o       (tl_sm1_53_us_d2h),
    .tl_d_o       (tl_sm1_53_ds_h2d),
    .tl_d_i       (tl_sm1_53_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_54 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_54_us_h2d),
    .tl_h_o       (tl_sm1_54_us_d2h),
    .tl_d_o       (tl_sm1_54_ds_h2d),
    .tl_d_i       (tl_sm1_54_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqDepth (4'h0),
    .DRspDepth (4'h0),
    .M         (2)
  ) u_sm1_55 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_55_us_h2d),
    .tl_h_o       (tl_sm1_55_us_d2h),
    .tl_d_o       (tl_sm1_55_ds_h2d),
    .tl_d_i       (tl_sm1_55_ds_d2h)
  );
  tlul_socket_m1 #(
    .HReqDepth (8'h0),
    .HRspDepth (8'h0),
    .DReqPass  (1'b0),
    .DRspPass  (1'b0),
    .M         (2)
  ) u_sm1_56 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_sm1_56_us_h2d),
    .tl_h_o       (tl_sm1_56_us_d2h),
    .tl_d_o       (tl_sm1_56_ds_h2d),
    .tl_d_i       (tl_sm1_56_ds_d2h)
  );
  tlul_socket_1n #(
    .HReqPass  (1'b0),
    .HRspPass  (1'b0),
    .DReqDepth (96'h0),
    .DRspDepth (96'h0),
    .N         (24)
  ) u_s1n_57 (
    .clk_i        (clk_main_i),
    .rst_ni       (rst_main_ni),
    .tl_h_i       (tl_s1n_57_us_h2d),
    .tl_h_o       (tl_s1n_57_us_d2h),
    .tl_d_o       (tl_s1n_57_ds_h2d),
    .tl_d_i       (tl_s1n_57_ds_d2h),
    .dev_select_i (dev_sel_s1n_57)
  );

endmodule
