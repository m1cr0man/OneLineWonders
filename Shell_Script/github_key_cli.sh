curl -u "$1" --data "{\"title\":\"arch-key\", \"key\":\"$(cat $2)\"}" https://api.github.com/user/keys
