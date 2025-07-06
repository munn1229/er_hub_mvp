# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
export PS1="[\u@\h \w]\$ "
export MYSQL_PS1="\h:\d>\_"

export PATH=$PATH:/composer/vendor/bin

alias cp="cp -i"
alias mv="mv -i"
alias rm="rm -i"
alias ll="ls -l"
alias la="ls -la"
