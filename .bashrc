#.bashrc
#ANSI colors
blackr="\e[0;30m"
blackb="\e[1;30m"
blacku="\e[4;30m"
biackba="\e[40m"
reset="\e[0m"
#Regular
rr="\e[0;31m"
gr="\e[0;32m"
yr="\e[0;33m"
br="\e[0;34m"
pr="\e[0;35m"
cr="\e[0;36m"
wr="\e[0;37m"
#Bold
rb="\e1;31m"
gb="\e1;32m"
yb="\e1;33m"
bb="\e1;34m"
pb="\e1;35m"
cb="\e1;36m"
wb="\e1;37m"
#Underline
ru="\e4;31m"
gu="\e4;32m"
yu="\e4;33m"
bu="\e4;34m"
pu="\e4;35m"
cu="\e4;36m"
wu="\e4;37m"
#Background
rba="\e41m"
gba="\e42m"
yba="\e43m"
bba="\e44m"
pba="\e[45m"
cba="\e46m"
wba="\e47m"
#Prompt
#Color variables must be wrapped with \[ \] for proper formatting
#PS1="\[\033[s\033[0;0H\[$pba\]\033[K\033[1;33m\t\033[0m\033[u\]"
PS1="\033[K\[$yr\]\h\\[$reset\]"	#Hostname 
PS1+="[\W]"	# [Directory] 
#PS1+="" # Git branch
export PS1
#export PS1="\e[2;37m\H\e[0m[\e[0;34m\W\e[0m]\n"

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
#Disable systemctl's auto-paging feature:
export SYSTEMD_PAGER=
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export HISTCONTROL=ignoredups
export HISTSIZE=1000
export XDG_CONFIG_HOME="$HOME/.config"
export VISUAL=vim
export EDITOR=vim
# source ~.git-promt.sh

#Alias
if [[ -f ~/.alias ]]; then
    . ~/.alias
fi
