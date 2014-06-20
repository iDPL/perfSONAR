# $Id$
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
# 
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log$

REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

## Download packages from EPEL

REPO_RPMS = 
PERFSONAR_BUNDLES = perfSONAR_PS-Bundles.spec
PERFSONAR_PKGS = $(shell cat $(PERFSONAR_BUNDLES) | sort | uniq | grep Requires: | awk '{printf("%s ", $$2) }')
PERFSONAR_PKGS += perl-perfSONAR_PS-Toolkit perl-perfSONAR_PS-perfAdmin 

EPEL_REPO_RPM = epel-release-6-8.noarch.rpm
REPO_RPMS += $(EPEL_REPO_RPM)
EPEL_REPO = epel.repo

INTERNET2_REPO_RPM = Internet2-repo-0.4-2.noarch.rpm
REPO_RPMS += $(INTERNET2_REPO_RPM)
INTERNET2_REPO = Internet2.repo


COMMA = ,
EMPTY = 
SPACE = $(EMPTY) $(EMPTY)
REPOS = $(EPEL_REPO) $(INTERNET2_REPO)
PS_REPOS = $(subst .repo,$(EMPTY),$(REPOS))
E_REPOS = base updates
E_REPOS += $(PS_REPOS)
ENABLED_REPOS= $(subst $(SPACE),$(COMMA),$(E_REPOS))

.PHONY: force RPMS local-config $(PERFSONAR_PKGS)

default: $(HOME)/.rpmmacros rpm-mkdirs RPMS 
	-yum -y install $(EPEL_REPO_RPM) $(INTERNET2_REPO_RPM) 
	for r in $(REPOS); do $(SED) -i 's/^enabled.*/enabled=0/' /etc/yum.repos.d/$$r; done
	$(MAKE) $(PERFSONAR_PKGS)
	-mkdir $(REDHAT.RPMS)/noarch
	-mkdir $(REDHAT.RPMS)/$(ARCH)
	$(INSTALL) RPMS/*noarch*rpm $(REDHAT.RPMS)/noarch
	$(INSTALL) $(REPO_RPMS) $(REDHAT.RPMS)/noarch
	$(INSTALL) RPMS/*$(ARCH)*rpm $(REDHAT.RPMS)/$(ARCH)
	$(MAKE) localrepo


perfSONAR.xml:
	echo "<kickstart>" > $@ 
	echo -e "\t<description>PerfSONAR Version $(VERSION) Packages </description>" >> $@
	for p in $(PERFSONAR_PKGS) $(patsubst %,%-repo,$(PS_REPOS)) ; do  \
		echo -e "\t<package>$$p</package>" >> $@; \
	done
	echo "</kickstart>" >> $@ 
	
	

localrepo: local-config
	cd RPMS; createrepo --basedir=. .

local-config: RPMS
	echo "[local]" > RPMS/local
	echo "name='perfSONAR Local Cache'" >> RPMS/local
	echo "baseurl=file:`pwd`/RPMS" >> RPMS/local
RPMS:
	-mkdir RPMS

$(PERFSONAR_PKGS): 
	yumdownloader --resolve --disablerepo='*' --enablerepo=$(ENABLED_REPOS) --destdir=RPMS $@

clean::
	/bin/rm -rf RPMS perfSONAR.xml
