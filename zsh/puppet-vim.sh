sudo apt-get install vim-puppet
sudo gem install puppet-lint
#ln -s /usr/share/vim/addons/syntax/puppet.vim ~/.vim/plugin/
#sudo vim-addons -w install puppet


# https://linuxaria.com/howto/use-vim-at-its-best-to-edit-your-puppet-manifests
cd ~
git clone https://github.com/ricciocri/vimrc .vim
mv .vim .vim.bak
cd .vim
git pull && git submodule init && git submodule update && git submodule status
cd ~
mv .vimrc .vimrc.bak
cp .vim/.vimrc .vimrc


