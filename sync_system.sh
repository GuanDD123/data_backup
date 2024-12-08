#!/bin/bash

rsync -avh --delete --no-specials\
    --exclude='桌面/' \
    --exclude='图片/' \
    --exclude='音乐/' \
    --exclude='视频/' \
    --exclude='文档/' \
    --exclude='下载/' \
    --exclude='Nutstore Files/' \
    --exclude='.wine/' \
    --exclude='.cache/' \
    --exclude='.local/share/Trash/' \
    --exclude='.local/share/Cryptomator/' \
    --exclude='*/mnt/*' \
    --exclude='.thumbnails/' \
    --exclude='.tmp/' \
    --exclude='.mozilla/firefox/*/cache2/' \
    --exclude='.config/google-chrome/Default/Cache/' \
    ~/ ~/.local/share/Cryptomator/mnt/Backup_tmp/home/
tar -czf ~/.local/share/Cryptomator/mnt/Backup_tmp/home.tar.gz -C ~/.local/share/Cryptomator/mnt/Backup_tmp home
rm -rf ~/.local/share/Cryptomator/mnt/Backup_tmp/home/
echo -e "\nhome/\n=====================\n"

rsync -avh --delete --no-specials\
    --exclude='apt/' \
    --exclude='udev/' \
    --exclude='init.d/' \
    --exclude='systemd/' \
    --exclude='mtab' \
    --exclude='selinux/' \
    --exclude='X11/' \
    --exclude='skel/' \
    --exclude='fstab' \
    --exclude='hostname' \
    --exclude='hosts' \
    --exclude='resolv.conf' \
    --exclude='ssh/' \
    --exclude='sudoers' \
    --exclude='sudoers.d/' \
    --exclude='network/' \
    --exclude='network/interfaces' \
    --exclude='cron.*' \
    --exclude='logrotate.d/' \
    --exclude='ssl/' \
    --exclude='pki/' \
    --exclude='tmpfiles.d/' \
    /etc/ ~/.local/share/Cryptomator/mnt/Backup_tmp/etc/
tar -czf ~/.local/share/Cryptomator/mnt/Backup_tmp/etc.tar.gz -C ~/.local/share/Cryptomator/mnt/Backup_tmp etc
rm -rf ~/.local/share/Cryptomator/mnt/Backup_tmp/etc/
echo -e "\n/etc/\n=====================\n"

rsync -avh --delete --no-specials\
    --include='*/' \
    --exclude='lib/*/tmp/' \
    --include='lib/mysql/**' \
    --include='lib/postgresql/**' \
    --include='www/**' \
    --include='mail/**' \
    --include='opt/**' \
    --exclude='*' \
    /var/ ~/.local/share/Cryptomator/mnt/Backup_tmp/var/
tar -czf ~/.local/share/Cryptomator/mnt/Backup_tmp/var.tar.gz -C ~/.local/share/Cryptomator/mnt/Backup_tmp var
rm -rf ~/.local/share/Cryptomator/mnt/Backup_tmp/var/
echo -e "\n/var/\n=====================\n"

rsync -avh --delete --no-specials\
    --include='*/' \
    --exclude='share/man/' \
    --exclude='share/doc/' \
    --exclude='share/icons/' \
    --exclude='share/locale/' \
    --include='share/**' \
    --include='bin/**' \
    --include='sbin/**' \
    --include='etc/**' \
    --include='lib/**' \
    --include='lib64/**' \
    --exclude='*' \
    /usr/local/ ~/.local/share/Cryptomator/mnt/Backup_tmp/usr_local/
tar -czf ~/.local/share/Cryptomator/mnt/Backup_tmp/usr_local.tar.gz -C ~/.local/share/Cryptomator/mnt/Backup_tmp usr_local
rm -rf ~/.local/share/Cryptomator/mnt/Backup_tmp/usr_local/
echo -e "\n/usr/local/\n=====================\n"

rsync -avh --delete ~/文档/Backup_tmp/ /media/sika/Expansion/00_Backup/
rm ~/.local/share/Cryptomator/mnt/Backup_tmp/*

dpkg --get-selections >~/.local/share/Cryptomator/mnt/00_Backup/installed-packages.list
