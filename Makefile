SOURCE_FILE := choose
TARGET_DIRS := $(shell find . -type d)

create_symlinks:
	@$(foreach dir,$(TARGET_DIRS),ln -s $(abspath $(SOURCE_FILE)) $(dir)/.$(SOURCE_FILE); chmod +x $(dir)/.$(SOURCE_FILE);) > /dev/null 2>&1

clean:
	@$(foreach dir,$(TARGET_DIRS),rm -f $(dir)/.$(SOURCE_FILE);) > /dev/null 2>&1