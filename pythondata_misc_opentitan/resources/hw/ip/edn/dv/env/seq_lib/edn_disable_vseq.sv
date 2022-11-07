// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

class edn_disable_vseq extends edn_base_vseq;
  `uvm_object_utils(edn_disable_vseq)
  `uvm_object_new

  push_pull_host_seq#(edn_pkg::FIPS_ENDPOINT_BUS_WIDTH)
      m_endpoint_pull_seq[MAX_NUM_ENDPOINTS];

  uint   num_requesters, num_ep_reqs, num_cs_reqs, wait_disable;

  task pre_start();
    // The edn_init is done in dut_init. So adding this disablement in pre_start in order to hit
    // certain boot init states.
    string main_sm_d_path = "tb.dut.u_edn_core.u_edn_main_sm.state_d";
    // TODO: This disable sequence targets at the boot mode only.
    state_e boot_sts[$] = {BootLoadIns, BootLoadGen, BootInsAckWait, BootCaptGenCnt,
                           BootSendGenCmd, BootGenAckWait, BootPulse, BootDone};

    // CSRNG requests will drop if disablement is sent.
    $assertoff(0, "tb.csrng_if.cmd_push_if.H_DataStableWhenValidAndNotReady_A");
    $assertoff(0, "tb.csrng_if.cmd_push_if.ValidHighUntilReady_A");

    fork
      begin
        // Wait until reset and clock are ready.
        wait(cfg.clk_rst_vif.rst_n == 1);
        cfg.clk_rst_vif.wait_clks(1);

        // Random delay, disable edn
        if ($urandom_range(0, 1)) begin
          `DV_CHECK_STD_RANDOMIZE_WITH_FATAL(wait_disable,
                                             wait_disable inside
                                             { [80:300] };)
           cfg.clk_rst_vif.wait_clks(wait_disable);
           `uvm_info(`gfn, $sformatf("Wait %0d clk cycles then issue edn disablement",
                     wait_disable), UVM_HIGH)
        end else begin
          bit [8:0] state_val;
          int rand_st_idx = $urandom_range(0, boot_sts.size()-1);
          `uvm_info(`gfn, $sformatf("Wait until %0s state then issue edn disablement",
                    boot_sts[rand_st_idx].name), UVM_HIGH)
          `DV_SPINWAIT(
              while (state_val != boot_sts[rand_st_idx]) begin
                uvm_hdl_read(main_sm_d_path, state_val);
                cfg.clk_rst_vif.wait_clks(1);
              end)
         end
        csr_wr(.ptr(ral.ctrl.edn_enable), .value(MuBi4False));
        cfg.clk_rst_vif.wait_clks($urandom_range(10, 50));
        // Enable edn
        csr_wr(.ptr(ral.ctrl.edn_enable), .value(MuBi4True));
      end
    join_none
    super.pre_start();
  endtask

  task body();
    super.body();
    num_requesters = cfg.num_endpoints;
    num_cs_reqs    = cfg.num_endpoints;
    num_ep_reqs    = num_cs_reqs * csrng_pkg::GENBITS_BUS_WIDTH/ENDPOINT_BUS_WIDTH;

    for (int i = 0; i < num_requesters; i++) begin
      // Create/Configure/Start endpoint_pull_seq
      m_endpoint_pull_seq[i] = push_pull_host_seq#(FIPS_ENDPOINT_BUS_WIDTH)::
          type_id::create($sformatf("m_endpoint_pull_seq[%0d]", i));
      m_endpoint_pull_seq[i].num_trans = num_ep_reqs;
    end

    // Start endpoint_pull sequences
    for (int i = 0; i < num_requesters; i++) begin
      automatic int j = i;
      fork
        begin
          m_endpoint_pull_seq[j].start
              (p_sequencer.endpoint_sequencer_h[j]);
        end
      join_none;
    end
  endtask

endclass
