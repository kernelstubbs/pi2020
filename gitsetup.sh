# Quick reference to getting the git repo set up with RSA keys
git config --global user.name "RPiInstructor"
git config --global user.email "pi@raspberry.pi"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# Assuming use of default key...if not generate keypair and replace
# upload id_rsa.pub to git deploy keys

git clone git@github.com:kernelstubbs/pi2020.git

# A normal clone won't work with keys - clone thusly