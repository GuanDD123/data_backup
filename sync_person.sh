rsync -avh --delete ~/桌面/.hidden/ ~/.local/share/Cryptomator/mnt/40_Documents/Desktop/.hidden/
echo -e "\n~/桌面/.hidden/\n=====================\n"

rsync -avh --delete ~/文档/Novels（自动）/ ~/.local/share/Cryptomator/mnt/40_Documents/Novels/
echo -e "\n~/文档/Novels（自动）/\n=====================\n"

rsync -avh --delete \
    --exclude='Cryptomator/' \
    ~/Nutstore\ Files/ ~/.local/share/Cryptomator/mnt/60_Nutstore/
echo -e "\n~/Nutstore\ Files/\n=====================\n"

rsync -avh --delete ~/Nutstore\ Files/Cryptomator/ /media/sika/Expansion/61_Cryptomator/
echo -e "\nCryptomator/\n=====================\n"
