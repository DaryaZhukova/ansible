FROM centos
RUN yum install -y systemd openssh-server net-tools && \
systemctl enable sshd
RUN useradd devops && \
echo devops | passwd devops --stdin
EXPOSE 22
VOLUME [ "/sys/fs/cgroup" ]
ENTRYPOINT ["/usr/sbin/init"]
