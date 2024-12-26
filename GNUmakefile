.PHONY: all

all: ladi.html
.PHONY: ladi.html
ladi.html:
	asciidoc -b xhtml11 -a data-uri -a icons --theme ladi -o ../ladi.github.io/ladi.html README.adoc

all: ladios-rockchip.html
.PHONY: ladios-rockchip.html
ladios-rockchip.html:
	asciidoc -b xhtml11 -a data-uri -a icons --theme ladi -o ../ladi.github.io/ladios-rockchip.html README.rockchip.adoc

all: ladios-pipewire.html
.PHONY: ladios-pipewire.html
ladios-pipewire.html:
	asciidoc -b xhtml11 -a data-uri -a icons --theme ladi -o ../ladi.github.io/ladios-pipewire.html README.pipewire.adoc

stage4:
	cd ../stagebuilder && ./autobuild.sh
