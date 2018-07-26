#!/usr/bash

set -e

opt1="--setup"
opt2="--setup-my"

install(){
    cd
    sudo apt-get install zsh
    cat /etc/shells
    chsh -s /bin/zsh
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
}

setup(){
    git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
    cd pi/pi_sh/
    cat zsh.txt >> ~/.zshrc
}

my_setup(){
    cat ./cfg/zsh.cfg >> ~/.zshrc
}

echo $1, 'wthf'

if [[ "$1" == "--setup" ]]
then
    echo 'setup'
    setup
elif [[ "$1" == "$opt2" ]]
then
    echo 'setup-my'
    my_setup
else
    echo 'install and setup'
    install
    setup
    my_setup
fi

echo $0,0
echo $1,1
echo $2,2
