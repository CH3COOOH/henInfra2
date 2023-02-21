chmod +x ./linux-amd64/*
cp ${PWD}/linux-amd64/* /usr/local/bin/
echo "Biniaries copied to /usr/local/bin/."
git reset --hard HEAD
