echo "Instalar zsh y git"
apt install zsh git -y
 
echo "Instalar oh-my-zsh"
cd $HOME &&
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
 
echo "Descargando autoload para vim..."
 
mkdir -p ~/.vim/autoload ~/.vim/bundle && \
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
 
echo "Configurando .vimrc..."
 
echo "execute pathogen#infect()
syntax on
filetype plugin indent on" > ~/.vimrc
 
echo "Clonando repo vim-puppet..."
cd ~/.vim/bundle && \
git clone https://github.com/rodjek/vim-puppet.git

