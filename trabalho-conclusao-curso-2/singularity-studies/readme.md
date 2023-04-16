## Passos para instalar o Singularity 3.11.1 no Ubuntu do zero

### caso erro de sudo:
```
su 
apt install sudo
usermod -aG sudo <username>
restart vm
```

### Instalação
```
sudo apt update && sudo apt install -y \
    build-essential \
    uuid-dev \
    libgpgme-dev \
    squashfs-tools \
    libseccomp-dev pkg-config squashfs-tools cryptsetup \
    wget \
    pkg-config \
    git \
    cryptsetup-bin \
    curl \
    libglib2.0-dev
    
# sudo rm -r /usr/local/go Only if go is already installed

export VERSION=1.19 OS=linux ARCH=amd64  # change this as you need

wget -O /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz https://dl.google.com/go/go${VERSION}.${OS}-${ARCH}.tar.gz && \
sudo tar -C /usr/local -xzf /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz

echo 'export GOPATH=${HOME}/go' >> ~/.bashrc && \
echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc && \
source ~/.bashrc

curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh |
sh -s -- -b $(go env GOPATH)/bin v1.21.0

mkdir -p ${GOPATH}/src/github.com/sylabs && \
cd ${GOPATH}/src/github.com/sylabs && \
git clone https://github.com/sylabs/singularity.git && \
cd singularity

git checkout v3.11.1

git submodule update --init

cd ${GOPATH}/src/github.com/sylabs/singularity && \
./mconfig && \
cd ./builddir && \
make && \
sudo make install

singularity version
```
