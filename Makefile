EXE=sendpitemp
DAEMON=sendpitempd
INSTALLDIR=/usr/local/bin

.phony: install

all:

install:
	cp -f $(EXE) $(INSTALLDIR)
	cp -f $(DAEMON) /etc/init.d
	@echo "To start at bootup run:"
	@echo "sudo update-rc.d sendpitempd defaults"   
