echo "unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefixset -g mode-mouse on
set -g mouse-select-window on
set -g mouse-select-pane on" > ~/.tmux.conf