rsync -avh --delete ~/桌面/.hidden/ ~/.local/share/Cryptomator/mnt/40_Documents/桌面/.hidden/

rsync -avh --delete ~/文档/Novels/ ~/.local/share/Cryptomator/mnt/40_Documents/Novels/

rsync -avh --delete \
    --exclude='Cryptomator/' \
    ~/Nutstore\ Files/ ~/.local/share/Cryptomator/mnt/60_Nutstore/

rsync -avh --delete ~/Nutstore\ Files/Cryptomator/ /media/sika/Expansion/61_Cryptomator/
