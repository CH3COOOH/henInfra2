chmod +x ./linux-amd64/*
ln -s ${PWD}/linux-amd64/* /usr/local/bin/
echo "Link generated."
git reset --hard HEAD
