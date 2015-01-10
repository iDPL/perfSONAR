%define relnum 2 
%define disttag pSPS

Version:		3.3.1
Name:			perfSONAR_PS-Bundles
Summary:		Bundles of the perfSONAR-PS Software
Release:		%{relnum}.%{disttag}
License:		Distributable, see LICENSE
Group:			Applications/Communications
URL:			http://psps.perfsonar.net/
BuildArch:		noarch

%description
Various bundles of the perfSONAR-PS Software

%package Level1
Summary:		pS-Performance Toolkit Bundle - Level 1
Group:			Applications/Communications
Requires:		bwctl-client
Requires:		bwctl-server
Requires:		ndt-client
Requires:		owamp-client
Requires:		owamp-server
Requires:		nuttcp
Requires:		iperf
Requires:               iperf3
Requires:		ntp
Requires2:		perl-Time-HiRes
Requires2:		perl-Archive-Tar
Requires2:		perl-Module-Load
Requires2:		perl-perfSONAR_PS-LSRegistrationDaemon
Requires2:		perl-perfSONAR_PS-Toolkit
Requires2:		perl-perfSONAR_PS-Toolkit-SystemEnvironment		

%description Level1
The perfSONAR Toolkit - Level 1 Bundle

%package Level2
Summary:		pS-Performance Toolkit Bundle - Level 2
Group:			Applications/Communications
Requires:		bwctl-client
Requires:		bwctl-server
Requires:		ndt-client
Requires:		owamp-client
Requires:		owamp-server
Requires:		nuttcp
Requires:		iperf
Requires:               iperf3
Requires:		ntp
Requires2:		perl-perfSONAR_PS-LSRegistrationDaemon
Requires2:		perl-perfSONAR_PS-Toolkit-SystemEnvironment		
Requires2:		perl-perfSONAR_PS-MeshConfig-Agent
Requires2:		perl-perfSONAR_PS-MeshConfig-GUIAgent
Requires2:	 	perl-perfSONAR_PS-MeshConfig-JSONBuilder	
Requires2:	 	perl-perfSONAR_PS-MeshConfig-Shared	
Requires2:	  	perl-perfSONAR-OPPD-MP-BWCTL
Requires2:		perl-perfSONAR-OPPD-MP-OWAMP
Requires2:		perl-perfSONAR-OPPD-MP-Shared
Requires2:		perl-perfSONAR-OPPD-MP-server

%description Level2
The perfSONAR Toolkit - Level 2 Bundle

%package maddash 
Summary:		pS-Performance Toolkit Bundle - maddash 
Group:			Applications/Communications
Requires2:		maddash	
Requires2:		maddash-server
Requires2:		maddash-webui


%post

%files
%defattr(0644,perfsonar,perfsonar,0755)

%files Level1
%defattr(0644,perfsonar,perfsonar,0755)

%files Level2
%defattr(0644,perfsonar,perfsonar,0755)

%files maddash
%defattr(0644,perfsonar,perfsonar,0755)

%changelog
* Thu Aug 01 2013 aaron@internet2.edu 3.3.1-1
- Initial bundle release
