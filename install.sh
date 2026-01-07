# Update the system first
sudo apt update && sudo apt upgrade -y

# Check the python version
installed="True"
[[python_version=$(python --version)]] || installed="False" && echo "Python is not installed, and will be installed shortly"

# Install python (may not always be run)
if [[$installed=="False"]]; then
    mkdir temp_python
    cd temp_python
    wget https://www.python.org/ftp/python/3.x.z/Python-3.14.2.tgz
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
       libncurses5-dev libncursesw5-dev xz-utils tk-dev
    tar xvf Python-3.14.2.tgz
    cd Python-3.14.2/
    ./configure --enable-optimizations --with-ensurepip=install
    mak -j 8
    sudo make altinstall
    python --version
    [[python_version=$(python --version)]] && cd && sudo rm -rf temp_python || echo "Python did not install correctly, please do it yourself"