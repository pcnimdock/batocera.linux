################################################################################
#
# guncon
#
################################################################################
GUNCON_VERSION = 0dfe0feaa2afc37a8a70f6cd0f6c803ee4d89f40
GUNCON_SITE = $(call github,pcnimdock,guncon3_dkms,$(GUNCON_VERSION))

define GUNCON_INSTALL_TARGET_CMDS
    $(INSTALL) -m 0644 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/controllers/guncon/99-guncon.rules $(TARGET_DIR)/etc/udev/rules.d/99-guncon.rules
    $(INSTALL) -m 0755 -D $(BR2_EXTERNAL_BATOCERA_PATH)/package/batocera/controllers/guncon/guncon-add      $(TARGET_DIR)/usr/bin/guncon-add
    $(INSTALL) -D -m 0755 $(@D)/calibration/calibrate.sh $(TARGET_DIR)/usr/bin/calibrate.sh
    $(INSTALL) -D -m 0755 $(@D)/calibration/calibrate.py $(TARGET_DIR)/usr/bin/calibrate.py
endef


$(eval $(kernel-module))
$(eval $(generic-package))
