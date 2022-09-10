// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// Note that this UNR only generate exclusions related to tlul_adapter_sram and FSM unreachables.
// A comprehensive UNR will be generated when achieving V3 stage.
//
//==================================================
// This file contains the Excluded objects
// Generated By User: chencindy
// Format Version: 2
// Date: Tue Feb  1 16:02:05 2022
// ExclMode: default
//==================================================
CHECKSUM: "2024123546 4210417746"
INSTANCE: tb.dut.u_tlul_adapter.u_rspfifo
ANNOTATION: "VC_COV_UNR"
Condition 1 "2331864568" "(gen_normal_fifo.full ? (1'(Depth)) : ((gen_normal_fifo.wptr_msb == gen_normal_fifo.rptr_msb) ? ((1'(gen_normal_fifo.wptr_value) - 1'(gen_normal_fifo.rptr_value))) : (((1'(Depth) - 1'(gen_normal_fifo.rptr_value)) + 1'(gen_normal_fifo.wptr_value))))) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 2 "1926118060" "((gen_normal_fifo.wptr_msb == gen_normal_fifo.rptr_msb) ? ((1'(gen_normal_fifo.wptr_value) - 1'(gen_normal_fifo.rptr_value))) : (((1'(Depth) - 1'(gen_normal_fifo.rptr_value)) + 1'(gen_normal_fifo.wptr_value)))) 1 -1" (1 "0")
ANNOTATION: "VC_COV_UNR"
Condition 3 "1937111844" "((gen_normal_fifo.fifo_empty && wvalid_i) ? wdata_i : gen_normal_fifo.storage_rdata) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 4 "4208363759" "(gen_normal_fifo.fifo_empty && wvalid_i) 1 -1" (1 "01")
ANNOTATION: "VC_COV_UNR"
Condition 4 "4208363759" "(gen_normal_fifo.fifo_empty && wvalid_i) 1 -1" (3 "11")
ANNOTATION: "VC_COV_UNR"
Condition 5 "2860893437" "(gen_normal_fifo.empty ? 'b0 : gen_normal_fifo.rdata_int) 1 -1" (1 "0")
CHECKSUM: "2024123546 3257640859"
INSTANCE: tb.dut.u_tlul_adapter.u_reqfifo
ANNOTATION: "VC_COV_UNR"
Condition 2 "1926118060" "((gen_normal_fifo.wptr_msb == gen_normal_fifo.rptr_msb) ? ((1'(gen_normal_fifo.wptr_value) - 1'(gen_normal_fifo.rptr_value))) : (((1'(Depth) - 1'(gen_normal_fifo.rptr_value)) + 1'(gen_normal_fifo.wptr_value)))) 1 -1" (1 "0")
CHECKSUM: "2024123546 95776463"
INSTANCE: tb.dut.u_tlul_adapter.u_sramreqfifo
ANNOTATION: "VC_COV_UNR"
Condition 1 "2331864568" "(gen_normal_fifo.full ? (1'(Depth)) : ((gen_normal_fifo.wptr_msb == gen_normal_fifo.rptr_msb) ? ((1'(gen_normal_fifo.wptr_value) - 1'(gen_normal_fifo.rptr_value))) : (((1'(Depth) - 1'(gen_normal_fifo.rptr_value)) + 1'(gen_normal_fifo.wptr_value))))) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 2 "1926118060" "((gen_normal_fifo.wptr_msb == gen_normal_fifo.rptr_msb) ? ((1'(gen_normal_fifo.wptr_value) - 1'(gen_normal_fifo.rptr_value))) : (((1'(Depth) - 1'(gen_normal_fifo.rptr_value)) + 1'(gen_normal_fifo.wptr_value)))) 1 -1" (1 "0")
ANNOTATION: "VC_COV_UNR"
Condition 3 "2329396864" "(gen_normal_fifo.empty ? 'b0 : gen_normal_fifo.rdata_int) 1 -1" (1 "0")
CHECKSUM: "3042386013 3871380215"
INSTANCE: tb.dut.u_tlul_adapter
ANNOTATION: "VC_COV_UNR"
Condition 3 "800561441" "((vld_rd_rsp && reqfifo_rdata.error) ? error_blanking_data : (vld_rd_rsp ? rspfifo_rdata.data : '0)) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 4 "2745829604" "(vld_rd_rsp && reqfifo_rdata.error) 1 -1" (2 "10")
ANNOTATION: "VC_COV_UNR"
Condition 4 "2745829604" "(vld_rd_rsp && reqfifo_rdata.error) 1 -1" (3 "11")
ANNOTATION: "VC_COV_UNR"
Condition 5 "1119953630" "(vld_rd_rsp ? rspfifo_rdata.data : '0) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 6 "561780173" "((vld_rd_rsp && reqfifo_rdata.error) ? error_blanking_integ : (vld_rd_rsp ? rspfifo_rdata.data_intg : prim_secded_pkg::SecdedInv3932ZeroEcc)) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 7 "3130851184" "(vld_rd_rsp && reqfifo_rdata.error) 1 -1" (2 "10")
ANNOTATION: "VC_COV_UNR"
Condition 7 "3130851184" "(vld_rd_rsp && reqfifo_rdata.error) 1 -1" (3 "11")
ANNOTATION: "VC_COV_UNR"
Condition 8 "2942914969" "(vld_rd_rsp ? rspfifo_rdata.data_intg : prim_secded_pkg::SecdedInv3932ZeroEcc) 1 -1" (2 "1")
ANNOTATION: "VC_COV_UNR"
Condition 13 "1798941048" "(d_valid && d_error) 1 -1" (1 "01")
ANNOTATION: "VC_COV_UNR"
Condition 16 "4228513916" "((((reqfifo_rdata.op == OpRead) & (~reqfifo_rdata.error))) ? reqfifo_rready : 1'b0) 1 -1" (2 "1")
CHECKSUM: "1413060523 1581044118"
INSTANCE: tb.dut.u_sha2
Fsm sha_st_q "2028159779"
ANNOTATION: "VC_COV_UNR"
Transition ShaUpdateDigest->ShaCompress "2->1"
CHECKSUM: "2024123546 2243903072"
INSTANCE: tb.dut.u_tlul_adapter.u_reqfifo
ANNOTATION: "VC_COV_UNR"
Branch 0 "1862733684" "gen_normal_fifo.full" (2) "gen_normal_fifo.full 0,0"
ANNOTATION: "VC_COV_UNR"
Branch 3 "2807735941" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 3 "2807735941" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1287846560" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1287846560" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
CHECKSUM: "2024123546 2243903072"
INSTANCE: tb.dut.u_tlul_adapter.u_sramreqfifo
ANNOTATION: "VC_COV_UNR"
Branch 0 "1862733684" "gen_normal_fifo.full" (0) "gen_normal_fifo.full 1,-"
ANNOTATION: "VC_COV_UNR"
Branch 0 "1862733684" "gen_normal_fifo.full" (2) "gen_normal_fifo.full 0,0"
ANNOTATION: "VC_COV_UNR"
Branch 1 "3867317506" "gen_normal_fifo.empty" (1) "gen_normal_fifo.empty 0"
ANNOTATION: "VC_COV_UNR"
Branch 3 "2807735941" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 3 "2807735941" "(!rst_ni)" (2) "(!rst_ni) 0,0,1,1"
ANNOTATION: "VC_COV_UNR"
Branch 3 "2807735941" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1287846560" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1287846560" "(!rst_ni)" (2) "(!rst_ni) 0,0,1,1"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1287846560" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
ANNOTATION: "VC_COV_UNR"
Branch 5 "2429929352" "gen_normal_fifo.fifo_incr_wptr" (0) "gen_normal_fifo.fifo_incr_wptr 1"
CHECKSUM: "2024123546 4157704780"
INSTANCE: tb.dut.u_tlul_adapter.u_rspfifo
ANNOTATION: "VC_COV_UNR"
Branch 0 "1862733684" "gen_normal_fifo.full" (0) "gen_normal_fifo.full 1,-"
ANNOTATION: "VC_COV_UNR"
Branch 0 "1862733684" "gen_normal_fifo.full" (2) "gen_normal_fifo.full 0,0"
ANNOTATION: "VC_COV_UNR"
Branch 1 "4156807255" "(gen_normal_fifo.fifo_empty && wvalid_i)" (0) "(gen_normal_fifo.fifo_empty && wvalid_i) 1"
ANNOTATION: "VC_COV_UNR"
Branch 2 "3867317506" "gen_normal_fifo.empty" (1) "gen_normal_fifo.empty 0"
ANNOTATION: "VC_COV_UNR"
Branch 4 "2807735941" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 4 "2807735941" "(!rst_ni)" (2) "(!rst_ni) 0,0,1,1"
ANNOTATION: "VC_COV_UNR"
Branch 4 "2807735941" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
ANNOTATION: "VC_COV_UNR"
Branch 5 "1287846560" "(!rst_ni)" (1) "(!rst_ni) 0,1,-,-"
ANNOTATION: "VC_COV_UNR"
Branch 5 "1287846560" "(!rst_ni)" (2) "(!rst_ni) 0,0,1,1"
ANNOTATION: "VC_COV_UNR"
Branch 5 "1287846560" "(!rst_ni)" (3) "(!rst_ni) 0,0,1,0"
ANNOTATION: "VC_COV_UNR"
Branch 6 "2429929352" "gen_normal_fifo.fifo_incr_wptr" (0) "gen_normal_fifo.fifo_incr_wptr 1"
CHECKSUM: "3042386013 2660487743"
INSTANCE: tb.dut.u_tlul_adapter
ANNOTATION: "VC_COV_UNR"
Branch 1 "1058271942" "(vld_rd_rsp && reqfifo_rdata.error)" (0) "(vld_rd_rsp && reqfifo_rdata.error) 1,-"
ANNOTATION: "VC_COV_UNR"
Branch 1 "1058271942" "(vld_rd_rsp && reqfifo_rdata.error)" (1) "(vld_rd_rsp && reqfifo_rdata.error) 0,1"
ANNOTATION: "VC_COV_UNR"
Branch 2 "1058271942" "(vld_rd_rsp && reqfifo_rdata.error)" (0) "(vld_rd_rsp && reqfifo_rdata.error) 1,-"
ANNOTATION: "VC_COV_UNR"
Branch 2 "1058271942" "(vld_rd_rsp && reqfifo_rdata.error)" (1) "(vld_rd_rsp && reqfifo_rdata.error) 0,1"
ANNOTATION: "VC_COV_UNR"
Branch 4 "1984420262" "((reqfifo_rdata.op == OpRead) & (~reqfifo_rdata.error))" (0) "((reqfifo_rdata.op == OpRead) & (~reqfifo_rdata.error)) 1"
ANNOTATION: "VC_COV_UNR"
Branch 5 "4197348121" "(!rst_ni)" (1) "(!rst_ni) 0,1"
ANNOTATION: "VC_COV_UNR"
Branch 6 "744749108" "reqfifo_rvalid" (1) "reqfifo_rvalid 1,0,1"
