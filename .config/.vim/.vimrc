filetype on
filetype plugin on
filetype indent on
syntax on

set nocompatible
set number
set cursorline

set shiftwidth=4
set tabstop=4
set expandtab

set nobackup
set scrolloff=10
set nowrap
set incsearch
set ignorecase
set smartcase
set showmode
set showmatch
set hlsearch
set history=1000
set wildmenu
set wildmode=list:longest
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

" Vimscripts --------------{{{

augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END
" }}}
