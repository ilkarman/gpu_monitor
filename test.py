test_data = b'<?xml version="1.0" ?>\n<!DOCTYPE nvidia_smi_log SYSTEM "nvsmi_device_v8.dtd">\n<nvidia_smi_log>\n\t<timestamp>Sat Jul 22 01:08:22 2017</timestamp>\n\t<driver_version>367.48</driver_version>\n\t<attached_gpus>4</attached_gpus>\n\t<gpu id="84AD:00:00.0">\n\t\t<product_name>Tesla M60</product_name>\n\t\t<product_brand>Tesla</product_brand>\n\t\t<display_mode>Enabled</display_mode>\n\t\t<display_active>Disabled</display_active>\n\t\t<persistence_mode>Disabled</persistence_mode>\n\t\t<accounting_mode>Disabled</accounting_mode>\n\t\t<accounting_mode_buffer_size>1920</accounting_mode_buffer_size>\n\t\t<driver_model>\n\t\t\t<current_dm>N/A</current_dm>\n\t\t\t<pending_dm>N/A</pending_dm>\n\t\t</driver_model>\n\t\t<serial>0324316153248</serial>\n\t\t<uuid>GPU-6eb29b6d-d878-9e20-02f4-b281f02a5395</uuid>\n\t\t<minor_number>0</minor_number>\n\t\t<vbios_version>84.04.85.00.04</vbios_version>\n\t\t<multigpu_board>No</multigpu_board>\n\t\t<board_id>0x84ad0000</board_id>\n\t\t<gpu_part_number>900-2G402-0310-030</gpu_part_number>\n\t\t<inforom_version>\n\t\t\t<img_version>G402.0060.00.04</img_version>\n\t\t\t<oem_object>1.1</oem_object>\n\t\t\t<ecc_object>3.0</ecc_object>\n\t\t\t<pwr_object>N/A</pwr_object>\n\t\t</inforom_version>\n\t\t<gpu_operation_mode>\n\t\t\t<current_gom>N/A</current_gom>\n\t\t\t<pending_gom>N/A</pending_gom>\n\t\t</gpu_operation_mode>\n\t\t<gpu_virtualization_mode>\n\t\t\t<virtualization_mode>Pass-Through</virtualization_mode>\n\t\t</gpu_virtualization_mode>\n\t\t<pci>\n\t\t\t<pci_bus>00</pci_bus>\n\t\t\t<pci_device>00</pci_device>\n\t\t\t<pci_domain>84AD</pci_domain>\n\t\t\t<pci_device_id>13F210DE</pci_device_id>\n\t\t\t<pci_bus_id>84AD:00:00.0</pci_bus_id>\n\t\t\t<pci_sub_system_id>115E10DE</pci_sub_system_id>\n\t\t\t<pci_gpu_link_info>\n\t\t\t\t<pcie_gen>\n\t\t\t\t\t<max_link_gen>3</max_link_gen>\n\t\t\t\t\t<current_link_gen>3</current_link_gen>\n\t\t\t\t</pcie_gen>\n\t\t\t\t<link_widths>\n\t\t\t\t\t<max_link_width>16x</max_link_width>\n\t\t\t\t\t<current_link_width>16x</current_link_width>\n\t\t\t\t</link_widths>\n\t\t\t</pci_gpu_link_info>\n\t\t\t<pci_bridge_chip>\n\t\t\t\t<bridge_chip_type>N/A</bridge_chip_type>\n\t\t\t\t<bridge_chip_fw>N/A</bridge_chip_fw>\n\t\t\t</pci_bridge_chip>\n\t\t\t<replay_counter>0</replay_counter>\n\t\t\t<tx_util>0 KB/s</tx_util>\n\t\t\t<rx_util>0 KB/s</rx_util>\n\t\t</pci>\n\t\t<fan_speed>N/A</fan_speed>\n\t\t<performance_state>P0</performance_state>\n\t\t<clocks_throttle_reasons>\n\t\t\t<clocks_throttle_reason_gpu_idle>Not Active</clocks_throttle_reason_gpu_idle>\n\t\t\t<clocks_throttle_reason_applications_clocks_setting>Active</clocks_throttle_reason_applications_clocks_setting>\n\t\t\t<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>\n\t\t\t<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>\n\t\t\t<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>\n\t\t\t<clocks_throttle_reason_unknown>Not Active</clocks_throttle_reason_unknown>\n\t\t</clocks_throttle_reasons>\n\t\t<fb_memory_usage>\n\t\t\t<total>8123 MiB</total>\n\t\t\t<used>7835 MiB</used>\n\t\t\t<free>288 MiB</free>\n\t\t</fb_memory_usage>\n\t\t<bar1_memory_usage>\n\t\t\t<total>256 MiB</total>\n\t\t\t<used>2 MiB</used>\n\t\t\t<free>254 MiB</free>\n\t\t</bar1_memory_usage>\n\t\t<compute_mode>Default</compute_mode>\n\t\t<utilization>\n\t\t\t<gpu_util>0 %</gpu_util>\n\t\t\t<memory_util>0 %</memory_util>\n\t\t\t<encoder_util>0 %</encoder_util>\n\t\t\t<decoder_util>0 %</decoder_util>\n\t\t</utilization>\n\t\t<ecc_mode>\n\t\t\t<current_ecc>Disabled</current_ecc>\n\t\t\t<pending_ecc>Disabled</pending_ecc>\n\t\t</ecc_mode>\n\t\t<ecc_errors>\n\t\t\t<volatile>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</volatile>\n\t\t\t<aggregate>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</aggregate>\n\t\t</ecc_errors>\n\t\t<retired_pages>\n\t\t\t<multiple_single_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</multiple_single_bit_retirement>\n\t\t\t<double_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</double_bit_retirement>\n\t\t\t<pending_retirement>No</pending_retirement>\n\t\t</retired_pages>\n\t\t<temperature>\n\t\t\t<gpu_temp>44 C</gpu_temp>\n\t\t\t<gpu_temp_max_threshold>91 C</gpu_temp_max_threshold>\n\t\t\t<gpu_temp_slow_threshold>88 C</gpu_temp_slow_threshold>\n\t\t</temperature>\n\t\t<power_readings>\n\t\t\t<power_state>P0</power_state>\n\t\t\t<power_management>Supported</power_management>\n\t\t\t<power_draw>40.78 W</power_draw>\n\t\t\t<power_limit>150.00 W</power_limit>\n\t\t\t<default_power_limit>150.00 W</default_power_limit>\n\t\t\t<enforced_power_limit>150.00 W</enforced_power_limit>\n\t\t\t<min_power_limit>112.50 W</min_power_limit>\n\t\t\t<max_power_limit>162.00 W</max_power_limit>\n\t\t</power_readings>\n\t\t<clocks>\n\t\t\t<graphics_clock>556 MHz</graphics_clock>\n\t\t\t<sm_clock>556 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>540 MHz</video_clock>\n\t\t</clocks>\n\t\t<applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</applications_clocks>\n\t\t<default_applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</default_applications_clocks>\n\t\t<max_clocks>\n\t\t\t<graphics_clock>1177 MHz</graphics_clock>\n\t\t\t<sm_clock>1177 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>1083 MHz</video_clock>\n\t\t</max_clocks>\n\t\t<clock_policy>\n\t\t\t<auto_boost>On</auto_boost>\n\t\t\t<auto_boost_default>On</auto_boost_default>\n\t\t</clock_policy>\n\t\t<supported_clocks>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>2505 MHz</value>\n\t\t\t\t<supported_graphics_clock>1177 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1152 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1126 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1101 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1076 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1050 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1025 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1000 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>975 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>949 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>924 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>911 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>899 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>873 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>848 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>823 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>785 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>759 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>734 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>709 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>683 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>658 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>633 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>608 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>582 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>557 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>532 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>324 MHz</value>\n\t\t\t\t<supported_graphics_clock>405 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t</supported_clocks>\n\t\t<processes>\n\t\t\t<process_info>\n\t\t\t\t<pid>42793</pid>\n\t\t\t\t<type>C</type>\n\t\t\t\t<process_name>python</process_name>\n\t\t\t\t<used_memory>7833 MiB</used_memory>\n\t\t\t</process_info>\n\t\t</processes>\n\t\t<accounted_processes>\n\t\t</accounted_processes>\n\t</gpu>\n\n\t<gpu id="9AEC:00:00.0">\n\t\t<product_name>Tesla M60</product_name>\n\t\t<product_brand>Tesla</product_brand>\n\t\t<display_mode>Enabled</display_mode>\n\t\t<display_active>Disabled</display_active>\n\t\t<persistence_mode>Disabled</persistence_mode>\n\t\t<accounting_mode>Disabled</accounting_mode>\n\t\t<accounting_mode_buffer_size>1920</accounting_mode_buffer_size>\n\t\t<driver_model>\n\t\t\t<current_dm>N/A</current_dm>\n\t\t\t<pending_dm>N/A</pending_dm>\n\t\t</driver_model>\n\t\t<serial>0324216096534</serial>\n\t\t<uuid>GPU-486a9476-a49e-fe6c-5696-61dc2e6c374f</uuid>\n\t\t<minor_number>3</minor_number>\n\t\t<vbios_version>84.04.85.00.04</vbios_version>\n\t\t<multigpu_board>No</multigpu_board>\n\t\t<board_id>0x9aec0000</board_id>\n\t\t<gpu_part_number>900-2G402-0310-030</gpu_part_number>\n\t\t<inforom_version>\n\t\t\t<img_version>G402.0060.00.04</img_version>\n\t\t\t<oem_object>1.1</oem_object>\n\t\t\t<ecc_object>3.0</ecc_object>\n\t\t\t<pwr_object>N/A</pwr_object>\n\t\t</inforom_version>\n\t\t<gpu_operation_mode>\n\t\t\t<current_gom>N/A</current_gom>\n\t\t\t<pending_gom>N/A</pending_gom>\n\t\t</gpu_operation_mode>\n\t\t<gpu_virtualization_mode>\n\t\t\t<virtualization_mode>Pass-Through</virtualization_mode>\n\t\t</gpu_virtualization_mode>\n\t\t<pci>\n\t\t\t<pci_bus>00</pci_bus>\n\t\t\t<pci_device>00</pci_device>\n\t\t\t<pci_domain>9AEC</pci_domain>\n\t\t\t<pci_device_id>13F210DE</pci_device_id>\n\t\t\t<pci_bus_id>9AEC:00:00.0</pci_bus_id>\n\t\t\t<pci_sub_system_id>115E10DE</pci_sub_system_id>\n\t\t\t<pci_gpu_link_info>\n\t\t\t\t<pcie_gen>\n\t\t\t\t\t<max_link_gen>3</max_link_gen>\n\t\t\t\t\t<current_link_gen>3</current_link_gen>\n\t\t\t\t</pcie_gen>\n\t\t\t\t<link_widths>\n\t\t\t\t\t<max_link_width>16x</max_link_width>\n\t\t\t\t\t<current_link_width>16x</current_link_width>\n\t\t\t\t</link_widths>\n\t\t\t</pci_gpu_link_info>\n\t\t\t<pci_bridge_chip>\n\t\t\t\t<bridge_chip_type>N/A</bridge_chip_type>\n\t\t\t\t<bridge_chip_fw>N/A</bridge_chip_fw>\n\t\t\t</pci_bridge_chip>\n\t\t\t<replay_counter>0</replay_counter>\n\t\t\t<tx_util>0 KB/s</tx_util>\n\t\t\t<rx_util>0 KB/s</rx_util>\n\t\t</pci>\n\t\t<fan_speed>N/A</fan_speed>\n\t\t<performance_state>P0</performance_state>\n\t\t<clocks_throttle_reasons>\n\t\t\t<clocks_throttle_reason_gpu_idle>Not Active</clocks_throttle_reason_gpu_idle>\n\t\t\t<clocks_throttle_reason_applications_clocks_setting>Active</clocks_throttle_reason_applications_clocks_setting>\n\t\t\t<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>\n\t\t\t<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>\n\t\t\t<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>\n\t\t\t<clocks_throttle_reason_unknown>Not Active</clocks_throttle_reason_unknown>\n\t\t</clocks_throttle_reasons>\n\t\t<fb_memory_usage>\n\t\t\t<total>8123 MiB</total>\n\t\t\t<used>7720 MiB</used>\n\t\t\t<free>403 MiB</free>\n\t\t</fb_memory_usage>\n\t\t<bar1_memory_usage>\n\t\t\t<total>256 MiB</total>\n\t\t\t<used>2 MiB</used>\n\t\t\t<free>254 MiB</free>\n\t\t</bar1_memory_usage>\n\t\t<compute_mode>Default</compute_mode>\n\t\t<utilization>\n\t\t\t<gpu_util>0 %</gpu_util>\n\t\t\t<memory_util>0 %</memory_util>\n\t\t\t<encoder_util>0 %</encoder_util>\n\t\t\t<decoder_util>0 %</decoder_util>\n\t\t</utilization>\n\t\t<ecc_mode>\n\t\t\t<current_ecc>Disabled</current_ecc>\n\t\t\t<pending_ecc>Disabled</pending_ecc>\n\t\t</ecc_mode>\n\t\t<ecc_errors>\n\t\t\t<volatile>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</volatile>\n\t\t\t<aggregate>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</aggregate>\n\t\t</ecc_errors>\n\t\t<retired_pages>\n\t\t\t<multiple_single_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</multiple_single_bit_retirement>\n\t\t\t<double_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</double_bit_retirement>\n\t\t\t<pending_retirement>No</pending_retirement>\n\t\t</retired_pages>\n\t\t<temperature>\n\t\t\t<gpu_temp>40 C</gpu_temp>\n\t\t\t<gpu_temp_max_threshold>91 C</gpu_temp_max_threshold>\n\t\t\t<gpu_temp_slow_threshold>88 C</gpu_temp_slow_threshold>\n\t\t</temperature>\n\t\t<power_readings>\n\t\t\t<power_state>P0</power_state>\n\t\t\t<power_management>Supported</power_management>\n\t\t\t<power_draw>41.13 W</power_draw>\n\t\t\t<power_limit>150.00 W</power_limit>\n\t\t\t<default_power_limit>150.00 W</default_power_limit>\n\t\t\t<enforced_power_limit>150.00 W</enforced_power_limit>\n\t\t\t<min_power_limit>112.50 W</min_power_limit>\n\t\t\t<max_power_limit>162.00 W</max_power_limit>\n\t\t</power_readings>\n\t\t<clocks>\n\t\t\t<graphics_clock>556 MHz</graphics_clock>\n\t\t\t<sm_clock>556 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>540 MHz</video_clock>\n\t\t</clocks>\n\t\t<applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</applications_clocks>\n\t\t<default_applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</default_applications_clocks>\n\t\t<max_clocks>\n\t\t\t<graphics_clock>1177 MHz</graphics_clock>\n\t\t\t<sm_clock>1177 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>1083 MHz</video_clock>\n\t\t</max_clocks>\n\t\t<clock_policy>\n\t\t\t<auto_boost>On</auto_boost>\n\t\t\t<auto_boost_default>On</auto_boost_default>\n\t\t</clock_policy>\n\t\t<supported_clocks>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>2505 MHz</value>\n\t\t\t\t<supported_graphics_clock>1177 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1152 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1126 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1101 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1076 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1050 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1025 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1000 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>975 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>949 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>924 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>911 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>899 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>873 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>848 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>823 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>785 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>759 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>734 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>709 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>683 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>658 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>633 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>608 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>582 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>557 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>532 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>324 MHz</value>\n\t\t\t\t<supported_graphics_clock>405 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t</supported_clocks>\n\t\t<processes>\n\t\t\t<process_info>\n\t\t\t\t<pid>42793</pid>\n\t\t\t\t<type>C</type>\n\t\t\t\t<process_name>python</process_name>\n\t\t\t\t<used_memory>7718 MiB</used_memory>\n\t\t\t</process_info>\n\t\t</processes>\n\t\t<accounted_processes>\n\t\t</accounted_processes>\n\t</gpu>\n\n\t<gpu id="A5D3:00:00.0">\n\t\t<product_name>Tesla M60</product_name>\n\t\t<product_brand>Tesla</product_brand>\n\t\t<display_mode>Enabled</display_mode>\n\t\t<display_active>Disabled</display_active>\n\t\t<persistence_mode>Disabled</persistence_mode>\n\t\t<accounting_mode>Disabled</accounting_mode>\n\t\t<accounting_mode_buffer_size>1920</accounting_mode_buffer_size>\n\t\t<driver_model>\n\t\t\t<current_dm>N/A</current_dm>\n\t\t\t<pending_dm>N/A</pending_dm>\n\t\t</driver_model>\n\t\t<serial>0324216096534</serial>\n\t\t<uuid>GPU-616d4955-3f63-edd4-3c63-242b8e3ed51f</uuid>\n\t\t<minor_number>1</minor_number>\n\t\t<vbios_version>84.04.85.00.03</vbios_version>\n\t\t<multigpu_board>No</multigpu_board>\n\t\t<board_id>0xa5d30000</board_id>\n\t\t<gpu_part_number>900-2G402-0310-030</gpu_part_number>\n\t\t<inforom_version>\n\t\t\t<img_version>G402.0060.00.04</img_version>\n\t\t\t<oem_object>1.1</oem_object>\n\t\t\t<ecc_object>3.0</ecc_object>\n\t\t\t<pwr_object>N/A</pwr_object>\n\t\t</inforom_version>\n\t\t<gpu_operation_mode>\n\t\t\t<current_gom>N/A</current_gom>\n\t\t\t<pending_gom>N/A</pending_gom>\n\t\t</gpu_operation_mode>\n\t\t<gpu_virtualization_mode>\n\t\t\t<virtualization_mode>Pass-Through</virtualization_mode>\n\t\t</gpu_virtualization_mode>\n\t\t<pci>\n\t\t\t<pci_bus>00</pci_bus>\n\t\t\t<pci_device>00</pci_device>\n\t\t\t<pci_domain>A5D3</pci_domain>\n\t\t\t<pci_device_id>13F210DE</pci_device_id>\n\t\t\t<pci_bus_id>A5D3:00:00.0</pci_bus_id>\n\t\t\t<pci_sub_system_id>115E10DE</pci_sub_system_id>\n\t\t\t<pci_gpu_link_info>\n\t\t\t\t<pcie_gen>\n\t\t\t\t\t<max_link_gen>3</max_link_gen>\n\t\t\t\t\t<current_link_gen>3</current_link_gen>\n\t\t\t\t</pcie_gen>\n\t\t\t\t<link_widths>\n\t\t\t\t\t<max_link_width>16x</max_link_width>\n\t\t\t\t\t<current_link_width>16x</current_link_width>\n\t\t\t\t</link_widths>\n\t\t\t</pci_gpu_link_info>\n\t\t\t<pci_bridge_chip>\n\t\t\t\t<bridge_chip_type>N/A</bridge_chip_type>\n\t\t\t\t<bridge_chip_fw>N/A</bridge_chip_fw>\n\t\t\t</pci_bridge_chip>\n\t\t\t<replay_counter>0</replay_counter>\n\t\t\t<tx_util>0 KB/s</tx_util>\n\t\t\t<rx_util>0 KB/s</rx_util>\n\t\t</pci>\n\t\t<fan_speed>N/A</fan_speed>\n\t\t<performance_state>P0</performance_state>\n\t\t<clocks_throttle_reasons>\n\t\t\t<clocks_throttle_reason_gpu_idle>Not Active</clocks_throttle_reason_gpu_idle>\n\t\t\t<clocks_throttle_reason_applications_clocks_setting>Active</clocks_throttle_reason_applications_clocks_setting>\n\t\t\t<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>\n\t\t\t<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>\n\t\t\t<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>\n\t\t\t<clocks_throttle_reason_unknown>Not Active</clocks_throttle_reason_unknown>\n\t\t</clocks_throttle_reasons>\n\t\t<fb_memory_usage>\n\t\t\t<total>8123 MiB</total>\n\t\t\t<used>7722 MiB</used>\n\t\t\t<free>401 MiB</free>\n\t\t</fb_memory_usage>\n\t\t<bar1_memory_usage>\n\t\t\t<total>256 MiB</total>\n\t\t\t<used>2 MiB</used>\n\t\t\t<free>254 MiB</free>\n\t\t</bar1_memory_usage>\n\t\t<compute_mode>Default</compute_mode>\n\t\t<utilization>\n\t\t\t<gpu_util>0 %</gpu_util>\n\t\t\t<memory_util>0 %</memory_util>\n\t\t\t<encoder_util>0 %</encoder_util>\n\t\t\t<decoder_util>0 %</decoder_util>\n\t\t</utilization>\n\t\t<ecc_mode>\n\t\t\t<current_ecc>Disabled</current_ecc>\n\t\t\t<pending_ecc>Disabled</pending_ecc>\n\t\t</ecc_mode>\n\t\t<ecc_errors>\n\t\t\t<volatile>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</volatile>\n\t\t\t<aggregate>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</aggregate>\n\t\t</ecc_errors>\n\t\t<retired_pages>\n\t\t\t<multiple_single_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</multiple_single_bit_retirement>\n\t\t\t<double_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</double_bit_retirement>\n\t\t\t<pending_retirement>No</pending_retirement>\n\t\t</retired_pages>\n\t\t<temperature>\n\t\t\t<gpu_temp>47 C</gpu_temp>\n\t\t\t<gpu_temp_max_threshold>91 C</gpu_temp_max_threshold>\n\t\t\t<gpu_temp_slow_threshold>88 C</gpu_temp_slow_threshold>\n\t\t</temperature>\n\t\t<power_readings>\n\t\t\t<power_state>P0</power_state>\n\t\t\t<power_management>Supported</power_management>\n\t\t\t<power_draw>41.15 W</power_draw>\n\t\t\t<power_limit>150.00 W</power_limit>\n\t\t\t<default_power_limit>150.00 W</default_power_limit>\n\t\t\t<enforced_power_limit>150.00 W</enforced_power_limit>\n\t\t\t<min_power_limit>112.50 W</min_power_limit>\n\t\t\t<max_power_limit>162.00 W</max_power_limit>\n\t\t</power_readings>\n\t\t<clocks>\n\t\t\t<graphics_clock>556 MHz</graphics_clock>\n\t\t\t<sm_clock>556 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>540 MHz</video_clock>\n\t\t</clocks>\n\t\t<applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</applications_clocks>\n\t\t<default_applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</default_applications_clocks>\n\t\t<max_clocks>\n\t\t\t<graphics_clock>1177 MHz</graphics_clock>\n\t\t\t<sm_clock>1177 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>1083 MHz</video_clock>\n\t\t</max_clocks>\n\t\t<clock_policy>\n\t\t\t<auto_boost>On</auto_boost>\n\t\t\t<auto_boost_default>On</auto_boost_default>\n\t\t</clock_policy>\n\t\t<supported_clocks>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>2505 MHz</value>\n\t\t\t\t<supported_graphics_clock>1177 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1152 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1126 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1101 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1076 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1050 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1025 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1000 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>975 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>949 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>924 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>911 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>899 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>873 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>848 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>823 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>785 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>759 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>734 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>709 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>683 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>658 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>633 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>608 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>582 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>557 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>532 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>324 MHz</value>\n\t\t\t\t<supported_graphics_clock>405 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t</supported_clocks>\n\t\t<processes>\n\t\t\t<process_info>\n\t\t\t\t<pid>42793</pid>\n\t\t\t\t<type>C</type>\n\t\t\t\t<process_name>python</process_name>\n\t\t\t\t<used_memory>7718 MiB</used_memory>\n\t\t\t</process_info>\n\t\t</processes>\n\t\t<accounted_processes>\n\t\t</accounted_processes>\n\t</gpu>\n\n\t<gpu id="B3C8:00:00.0">\n\t\t<product_name>Tesla M60</product_name>\n\t\t<product_brand>Tesla</product_brand>\n\t\t<display_mode>Enabled</display_mode>\n\t\t<display_active>Disabled</display_active>\n\t\t<persistence_mode>Disabled</persistence_mode>\n\t\t<accounting_mode>Disabled</accounting_mode>\n\t\t<accounting_mode_buffer_size>1920</accounting_mode_buffer_size>\n\t\t<driver_model>\n\t\t\t<current_dm>N/A</current_dm>\n\t\t\t<pending_dm>N/A</pending_dm>\n\t\t</driver_model>\n\t\t<serial>0324316153248</serial>\n\t\t<uuid>GPU-aa87804c-30d1-5cd4-a6df-96a75384d437</uuid>\n\t\t<minor_number>2</minor_number>\n\t\t<vbios_version>84.04.85.00.03</vbios_version>\n\t\t<multigpu_board>No</multigpu_board>\n\t\t<board_id>0xb3c80000</board_id>\n\t\t<gpu_part_number>900-2G402-0310-030</gpu_part_number>\n\t\t<inforom_version>\n\t\t\t<img_version>G402.0060.00.04</img_version>\n\t\t\t<oem_object>1.1</oem_object>\n\t\t\t<ecc_object>3.0</ecc_object>\n\t\t\t<pwr_object>N/A</pwr_object>\n\t\t</inforom_version>\n\t\t<gpu_operation_mode>\n\t\t\t<current_gom>N/A</current_gom>\n\t\t\t<pending_gom>N/A</pending_gom>\n\t\t</gpu_operation_mode>\n\t\t<gpu_virtualization_mode>\n\t\t\t<virtualization_mode>Pass-Through</virtualization_mode>\n\t\t</gpu_virtualization_mode>\n\t\t<pci>\n\t\t\t<pci_bus>00</pci_bus>\n\t\t\t<pci_device>00</pci_device>\n\t\t\t<pci_domain>B3C8</pci_domain>\n\t\t\t<pci_device_id>13F210DE</pci_device_id>\n\t\t\t<pci_bus_id>B3C8:00:00.0</pci_bus_id>\n\t\t\t<pci_sub_system_id>115E10DE</pci_sub_system_id>\n\t\t\t<pci_gpu_link_info>\n\t\t\t\t<pcie_gen>\n\t\t\t\t\t<max_link_gen>3</max_link_gen>\n\t\t\t\t\t<current_link_gen>3</current_link_gen>\n\t\t\t\t</pcie_gen>\n\t\t\t\t<link_widths>\n\t\t\t\t\t<max_link_width>16x</max_link_width>\n\t\t\t\t\t<current_link_width>16x</current_link_width>\n\t\t\t\t</link_widths>\n\t\t\t</pci_gpu_link_info>\n\t\t\t<pci_bridge_chip>\n\t\t\t\t<bridge_chip_type>N/A</bridge_chip_type>\n\t\t\t\t<bridge_chip_fw>N/A</bridge_chip_fw>\n\t\t\t</pci_bridge_chip>\n\t\t\t<replay_counter>0</replay_counter>\n\t\t\t<tx_util>0 KB/s</tx_util>\n\t\t\t<rx_util>0 KB/s</rx_util>\n\t\t</pci>\n\t\t<fan_speed>N/A</fan_speed>\n\t\t<performance_state>P0</performance_state>\n\t\t<clocks_throttle_reasons>\n\t\t\t<clocks_throttle_reason_gpu_idle>Not Active</clocks_throttle_reason_gpu_idle>\n\t\t\t<clocks_throttle_reason_applications_clocks_setting>Active</clocks_throttle_reason_applications_clocks_setting>\n\t\t\t<clocks_throttle_reason_sw_power_cap>Not Active</clocks_throttle_reason_sw_power_cap>\n\t\t\t<clocks_throttle_reason_hw_slowdown>Not Active</clocks_throttle_reason_hw_slowdown>\n\t\t\t<clocks_throttle_reason_sync_boost>Not Active</clocks_throttle_reason_sync_boost>\n\t\t\t<clocks_throttle_reason_unknown>Not Active</clocks_throttle_reason_unknown>\n\t\t</clocks_throttle_reasons>\n\t\t<fb_memory_usage>\n\t\t\t<total>8123 MiB</total>\n\t\t\t<used>7722 MiB</used>\n\t\t\t<free>401 MiB</free>\n\t\t</fb_memory_usage>\n\t\t<bar1_memory_usage>\n\t\t\t<total>256 MiB</total>\n\t\t\t<used>2 MiB</used>\n\t\t\t<free>254 MiB</free>\n\t\t</bar1_memory_usage>\n\t\t<compute_mode>Default</compute_mode>\n\t\t<utilization>\n\t\t\t<gpu_util>0 %</gpu_util>\n\t\t\t<memory_util>0 %</memory_util>\n\t\t\t<encoder_util>0 %</encoder_util>\n\t\t\t<decoder_util>0 %</decoder_util>\n\t\t</utilization>\n\t\t<ecc_mode>\n\t\t\t<current_ecc>Disabled</current_ecc>\n\t\t\t<pending_ecc>Disabled</pending_ecc>\n\t\t</ecc_mode>\n\t\t<ecc_errors>\n\t\t\t<volatile>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</volatile>\n\t\t\t<aggregate>\n\t\t\t\t<single_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</single_bit>\n\t\t\t\t<double_bit>\n\t\t\t\t\t<device_memory>N/A</device_memory>\n\t\t\t\t\t<register_file>N/A</register_file>\n\t\t\t\t\t<l1_cache>N/A</l1_cache>\n\t\t\t\t\t<l2_cache>N/A</l2_cache>\n\t\t\t\t\t<texture_memory>N/A</texture_memory>\n\t\t\t\t\t<texture_shm>N/A</texture_shm>\n\t\t\t\t\t<total>N/A</total>\n\t\t\t\t</double_bit>\n\t\t\t</aggregate>\n\t\t</ecc_errors>\n\t\t<retired_pages>\n\t\t\t<multiple_single_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</multiple_single_bit_retirement>\n\t\t\t<double_bit_retirement>\n\t\t\t\t<retired_count>0</retired_count>\n\t\t\t\t<retired_page_addresses>\n\t\t\t\t</retired_page_addresses>\n\t\t\t</double_bit_retirement>\n\t\t\t<pending_retirement>No</pending_retirement>\n\t\t</retired_pages>\n\t\t<temperature>\n\t\t\t<gpu_temp>50 C</gpu_temp>\n\t\t\t<gpu_temp_max_threshold>91 C</gpu_temp_max_threshold>\n\t\t\t<gpu_temp_slow_threshold>88 C</gpu_temp_slow_threshold>\n\t\t</temperature>\n\t\t<power_readings>\n\t\t\t<power_state>P0</power_state>\n\t\t\t<power_management>Supported</power_management>\n\t\t\t<power_draw>42.37 W</power_draw>\n\t\t\t<power_limit>150.00 W</power_limit>\n\t\t\t<default_power_limit>150.00 W</default_power_limit>\n\t\t\t<enforced_power_limit>150.00 W</enforced_power_limit>\n\t\t\t<min_power_limit>112.50 W</min_power_limit>\n\t\t\t<max_power_limit>162.00 W</max_power_limit>\n\t\t</power_readings>\n\t\t<clocks>\n\t\t\t<graphics_clock>556 MHz</graphics_clock>\n\t\t\t<sm_clock>556 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>540 MHz</video_clock>\n\t\t</clocks>\n\t\t<applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</applications_clocks>\n\t\t<default_applications_clocks>\n\t\t\t<graphics_clock>557 MHz</graphics_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t</default_applications_clocks>\n\t\t<max_clocks>\n\t\t\t<graphics_clock>1177 MHz</graphics_clock>\n\t\t\t<sm_clock>1177 MHz</sm_clock>\n\t\t\t<mem_clock>2505 MHz</mem_clock>\n\t\t\t<video_clock>1083 MHz</video_clock>\n\t\t</max_clocks>\n\t\t<clock_policy>\n\t\t\t<auto_boost>On</auto_boost>\n\t\t\t<auto_boost_default>On</auto_boost_default>\n\t\t</clock_policy>\n\t\t<supported_clocks>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>2505 MHz</value>\n\t\t\t\t<supported_graphics_clock>1177 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1152 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1126 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1101 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1076 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1050 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1025 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>1000 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>975 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>949 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>924 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>911 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>899 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>873 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>848 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>823 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>785 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>759 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>734 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>709 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>683 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>658 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>633 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>608 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>582 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>557 MHz</supported_graphics_clock>\n\t\t\t\t<supported_graphics_clock>532 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t\t<supported_mem_clock>\n\t\t\t\t<value>324 MHz</value>\n\t\t\t\t<supported_graphics_clock>405 MHz</supported_graphics_clock>\n\t\t\t</supported_mem_clock>\n\t\t</supported_clocks>\n\t\t<processes>\n\t\t\t<process_info>\n\t\t\t\t<pid>42793</pid>\n\t\t\t\t<type>C</type>\n\t\t\t\t<process_name>python</process_name>\n\t\t\t\t<used_memory>7718 MiB</used_memory>\n\t\t\t</process_info>\n\t\t</processes>\n\t\t<accounted_processes>\n\t\t</accounted_processes>\n\t</gpu>\n\n</nvidia_smi_log>\n'
