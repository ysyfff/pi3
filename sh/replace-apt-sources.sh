#su -s 

sudo echo -e  "deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi \n deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi" > /etc/apt/sources.list

sudo echo -e "deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/ stretch main ui" > /etc/apt/sources.list.d/raspi.list

sudo apt update && sudo apt -y upgrade
