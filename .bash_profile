
# ~/.bash_profile: executed by bash(1) for login shells.
# CSL default
# by kkowal 2005-06-21

# the default umask is set in /etc/login.defs
umask 022

# include .bashrc if it exists
[ -f ~/.bashrc ] && . ~/.bashrc

# color
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \$ '

# Adds color to ls command output
alias ls='ls -G'
alias ditaa='java -jar /opt/homebrew/Cellar/ditaa/0.11.0_1/libexec/ditaa-0.11.0-standalone.jar'

export EDITOR=vim




PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"

#export PATH=$PATH:/usr/local/bin:/Library/ODBC/instantclient_12_2 
export ORACLE_HOME=/Users/jmkrone/Setup/instantclient_12_2/sdk/oracle
export DYLD_LIBRARY_PATH=/Library/ODBC/instantclient_12_2 
export TNS_ADMIN=/Library/ODBC/instantclient_12_2/network/admin 
export CLASSPATH=$CLASSPATH:$ORACLE_HOME
export NLS_LANG="English_Australia.UTF8"

export PATH=/usr/local/bin:/usr/local/sbin:$PATH

export PYTHONPATH=/usr/local/bin/



### Used for Yeoman
NPM_PACKAGES="${HOME}/.npm-packages"

export PATH="$NPM_PACKAGES/bin:$PATH"

# Unset manpath so we can inherit from /etc/manpath via the `manpath` command
unset MANPATH # delete if you already modified MANPATH elsewhere in your config
export MANPATH="$NPM_PACKAGES/share/man:$(manpath)"


# end


# This was here before bash_profile was copied from desktop mac

export NLS_LANG="/Users/jmkrone/instantclient_12_2/"
export DYLD_LIBRARY_PATH="/Users/jmkrone/instantclient_12_2/"


export TSN_ADMIN="/Users/jmkrone/instantclient_12_2/network/admin"

#
# Run /usr/libexec/java_home -V for details on installed packages
#
# Java 8
#export JAVA_HOME=$(/usr/libexec/java_home -v 1.8.0_211)

# Java 15 - adoptopenjdk-16
export JAVA_HOME=$(/usr/libexec/java_home -v 16)

export PATH=~/Users/jmkrone/instantclient_12_2:$PATH




export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

export PATH=/usr/local/smlnj/bin:"$PATH"
eval "$(/opt/homebrew/bin/brew shellenv)"
