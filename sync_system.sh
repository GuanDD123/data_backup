#!/bin/bash

rsync -avh --delete \
    --exclude='桌面/' \
    --exclude='图片/' \
    --exclude='音乐/' \
    --exclude='视频/' \
    --exclude='文档/' \
    --exclude='下载/' \
    --exclude='Nutstore Files/' \
    --exclude='.cache/' \
    --exclude='.local/share/Trash/' \
    --exclude='.local/share/Cryptomator/' \
    --exclude='.thumbnails/' \
    --exclude='.tmp/' \
    --exclude='.mozilla/firefox/*/cache2/' \
    --exclude='.config/google-chrome/Default/Cache/' \
    ~/ ~/.local/share/Cryptomator/mnt/00_Backup/home/

rsync -avh --delete \
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
    /etc/ ~/.local/share/Cryptomator/mnt/00_Backup/etc/

rsync -avh --delete \
    --include='*/' \
    --exclude='lib/*/tmp/' \
    --include='lib/mysql/**' \
    --include='lib/postgresql/**' \
    --include='www/**' \
    --include='mail/**' \
    --include='opt/**' \
    --exclude='*' \
    /var/ ~/.local/share/Cryptomator/mnt/00_Backup/var/

rsync -avh --delete \
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
    /usr/local/ ~/.local/share/Cryptomator/mnt/00_Backup/usr_local/

dpkg --get-selections >~/.local/share/Cryptomator/mnt/00_Backup/installed-packages.list
