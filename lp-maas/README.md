lp-maas
---

maas-image-builder
===
Since MaaS 1.7, CentOS images are officially supported to be installed by
Curtin (which simply dd's images to local disk, so technically any installed
image could be used). The following install guide should work as of December
2015. The official documentation is constantly out of date or incomplete.

```
apt-get install bzr make
bzr branch lp:maas-image-builder

make install-dependencies
python setup.py build
sudo python setup.py install

sudo apt-get install ebtables
sudo systemctl restart libvirtd
(sudo virsh net-start default)
sudo maas-image-builder -a amd64 --output centos-amd64 centos
```

When dealing with hardware that requires specific kernel modules to boot, these
will have to be added to the initramfs inside the image. Modify the CentOS7
kickstart file in the maas-image-builder source tree as follows:

```
# in %post

# add extra drivers to initrd
# storage drivers won't be detected by dracut when kickstarting in a kvm
echo 'add_drivers+="hpsa"' > /etc/dracut.conf.d/extra-drivers.conf
KERNEL_VERSION=$(rpm -q kernel --qf '%{version}-%{release}.%{arch}\n')
/sbin/dracut -f /boot/initramfs-$KERNEL_VERSION.img $KERNEL_VERSION
```
