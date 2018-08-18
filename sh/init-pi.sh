#!/usr/bash

# 重要！重要！重要！请看tip

# tip1: 有些执行需要sudo权限，所以先执行su，在root账户中(状态下) 执行此文件
# tip2: 进入pi3目录，执行 su，执行sh init-pi.sh
# tip3: bash是sh的增强版本，所以请使用bash执行sh脚本

# 1. setup git
ssh-keygen
cat ~/.ssh/id_rsa.pub

# 2. setup apt-get sourcelist
bash sh/replace-apt-sources.sh

# 3. install zsh
curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh

# 4. setup zsh
bash /sh/zsh.sh
