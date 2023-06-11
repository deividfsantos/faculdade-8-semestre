# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@18.234.84.140:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@52.90.24.139:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@54.147.13.65:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@54.242.240.237:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@54.234.250.129:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@54.91.93.79:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@18.209.62.191:~
# scp -i /home/deivid/Documents/ec2/ec2cluster.pem $1 ubuntu@107.22.119.55:~

# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@34.230.84.156 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@54.90.106.11 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@18.232.150.122 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@18.234.86.81 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@54.90.65.224 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@35.175.173.161 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@54.91.108.58 'sudo umount /dev/loop*'
# ssh -i /home/deivid/Documents/ec2/ec2cluster.pem ubuntu@34.224.218.23 'sudo umount /dev/loop*'

scp -i /home/deivid/Documents/ec2/ec2cluster.pem  ubuntu@34.230.84.156:~/output.txt .
