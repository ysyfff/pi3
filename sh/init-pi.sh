# 有些执行需要sudo权限，所以先执行su，在root账户中(状态下) 执行此文件
# 0. 进入pi3目录，执行 su，执行sh init-pi.sh

# 1. setup git
ssh-keygen
cat ~/.ssh/id_rsa.pub

# 2. setup apt-get sourcelist
bash sh/replace-apt-sources.sh

# 3. install zsh
curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh

# 4. setup zsh
bash /sh/zsh.sh
