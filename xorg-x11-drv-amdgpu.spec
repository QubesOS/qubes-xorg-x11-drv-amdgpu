%global tarball xf86-video-amdgpu
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

# Suppress output of debuginfo and debugsource
%global debug_package %{nil}

# Xorg cannot load hardened build
%undefine _hardened_build

Name:       xorg-x11-drv-amdgpu
Version:    22.0.0
Release:    1%{?dist}

Summary:    AMD GPU video driver
License:    MIT

URL:        https://www.x.org/wiki
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz

ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: xorg-x11-server-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libdrm-devel
BuildRequires: kernel-headers
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: libudev-devel
BuildRequires: xorg-x11-glamor-devel

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libdrm >= 2.4.89

%description
X.Org X11 AMDGPU driver

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
#autoreconf -fiv
%configure --disable-static --enable-glamor
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{driverdir}/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*

%changelog
* Mon Mar 14 2022 Christopher Atherton <atherchris@gmail.com> - 22.0.0-1
- Update to 22.0.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug  4 2021 Christopher Atherton <atherchris@gmail.com> - 21.0.0-1
- Update to 21.0.0

* Mon Apr 19 2021 Christopher Atherton <atherchris@gmail.com> - 19.1.0-8
- Remove dri.h includes and use xf86drm.h

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 09:38:10 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 19.1.0-6
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Petr Viktorin <pviktori@redhat.com> - 19.1.0-4
- Remove BuildRequires on python2

* Thu Feb 06 2020 Adam Jackson <ajax@redhat.com> - 19.1.0-3
- Fix link failure with gcc 10

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Christopher Atherton <the8lack8ox@gmail.com> - 19.1.0-1
- Update to 19.1.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Christopher Atherton <the8lack8ox@gmail.com> - 19.0.1-1
- Update to 19.0.1

* Wed Mar 06 2019 Christopher Atherton <the8lack8ox@gmail.com> - 19.0.0-1
- Update to 19.0.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Christopher Atherton <the8lack8ox@gmail.com> - 18.1.0-1
- Update to 18.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 18.0.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 18.0.1-2
- Rebuild for xserver 1.20

* Thu Mar 15 2018 Christopher Atherton <the8lack8ox@gmail.com> - 18.0.1-1
- Update to 18.0.1

* Wed Mar 07 2018 Christopher Atherton <the8lack8ox@gmail.com> - 18.0.0-1
- Update to 18.0.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Christopher Atherton <the8lack8ox@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 poma <poma@gmail.com> 1.3.0-1
- Update to 1.3.0

* Mon Nov 21 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.2.0-1
- Update to latest release

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> 1.1.2-3
- Update to latest git master for use with xserver-1.19
- Rebuild against xserver-1.19

* Sat Sep 24 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.2-2
- Use upstream provided xorg.conf file

* Sat Sep 17 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.2-1
- Update to latest release

* Thu Sep 15 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.1-1
- Update to latest release

* Sun Sep 04 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.0-6
- Add BuildRequires on mesa-libgbm-devel

* Sun Sep 04 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.0-5
- Disable hardened build

* Sun Sep 04 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.0-4
- Use buildroot macro not RPM_BUILD_ROOT variable
- Replace /usr/share with _datadir
- Enable hardened build

* Sat Sep 03 2016 Christopher Atherton <the8lack8ox@gmail.cmo> 1.1.0-3
- Require libdrm equal to or later than 2.4.63

* Sat Sep 03 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.0-2
- Fixed ExcludeArch typo
- Add URL for source
- Use --force with autoreconf
- Use make_build macro
- Removed explicit libdrm dependency

* Sat Sep 03 2016 Christopher Atherton <the8lack8ox@gmail.com> 1.1.0-1
- Initial spec
