FROM centos:7

RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm && \
  yum install -y \
  puppet-server \
  telnet \
  bind-utils \
  tree \
  git \
  tree \
  vim

RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \
  curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

RUN echo -e 'execute pathogen#infect()\nsyntax on\nfiletype plugin indent on\nset number' > ~/.vimrc

RUN cd ~/.vim/bundle; git clone https://github.com/rodjek/vim-puppet.git ;\
  git clone git://github.com/godlygeek/tabular.git

# When using docker::run make sure to add { restarts => 'no' } to prevent using
# upstart/systemd managment, which will break in docker container.
RUN puppet module install puppetlabs-docker_platform

RUN echo "alias ls='ls --color'" >> ~/.bashrc

WORKDIR /etc/puppet/modules

ADD puppet.conf /etc/puppet/puppet.conf

CMD puppet master --verbose --debug --no-daemonize
