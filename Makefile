EXE=sendpitemp sendpressure readExtTemp.py sendExtTemp
DAEMON=sendpitempd sendpressured sendExtTempd
INSTALLDIR=/usr/local/bin

.phony: install

all:

install:
	cp -f $(EXE) $(INSTALLDIR)
	cp -f $(DAEMON) /etc/init.d
	@echo "To start at bootup run:"
	@echo "sudo update-rc.d sendpitempd defaults"   
	@echo "sudo update-rc.d sendpressured defaults"   
	@echo "sudo update-rc.d sendExtTempd defaults"   

