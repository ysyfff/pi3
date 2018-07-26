
set -e

curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh

sudo -s
echo -e "deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi \n deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi" > /etc/apt/sources.list
echo -e "deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/ stretch main ui" > /etc/apt/sources.list.d/raspi.list
exit
sudo apt update && sudo apt -y upgrade
