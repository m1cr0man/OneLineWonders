curl -u "$1" --data "{\"title\":\"$3\", \"key\":\"$(cat $2)\"}" https://api.github.com/user/keys
# usage: ./github_key_cli.sh username key_location name_of_key_lel
