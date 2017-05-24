#-*-coding: utf-8 -*-
import os, sys, time
import paramiko
import urllib2

def init_web(ip_address,sshkeyfilename,keylocation):

    sshuser = 'ec2-user'
    os.chdir(keylocation)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    sys.stderr.write("ip=" + ip_address)
    
    ssh.connect(hostname=ip_address,username=sshuser,key_filename=sshkeyfilename)
    #make folder
    stdin, stdout, stderr = ssh.exec_command("sudo mkdir /usr/share/tomcat6-myapp")
    stdin.flush()
    data = stdout.read().splitlines()
    print ""

    #make folder
    stdin, stdout, stderr = ssh.exec_command("sudo mkdir /usr/share/tomcat6-myapp/MyWebApp")
    stdin.flush()
    data = stdout.read().splitlines()
    
    #Create index file
    stdin, stdout, stderr = ssh.exec_command("sudo bash -c 'echo hello world! > /usr/share/tomcat6-myapp/MyWebApp/index.html'")
    stdin.flush()
    data = stdout.read().splitlines()

    #Create index file
    stdin, stdout, stderr = ssh.exec_command("sudo bash -c 'echo hello world! > /usr/share/tomcat6-myapp/MyWebApp/MyPage.html'")
    stdin.flush()
    data = stdout.read().splitlines()
    
    
    stdin, stdout, stderr = ssh.exec_command("sudo bash -c 'echo \<Context path=\\\"/MyWebApp\\\" docBase=\\\"/usr/share/tomcat6-myapp/MyWebApp\\\"/\> > /etc/tomcat6/Catalina/localhost/MyWebApp.xml'")
    stdin.flush()
    data = stdout.read().splitlines()

    #print xml_content
    stdin, stdout, stderr = ssh.exec_command("sudo bash -c 'echo \<Context path=\\\"/MyPage\\\" docBase=\\\"/usr/share/tomcat6-myapp/MyWebApp/MyPage\\\"/\> > /etc/tomcat6/Catalina/localhost/MyPage.xml'")
    stdin.flush()
    data = stdout.read().splitlines()


if __name__=='__main__':
    sys.stderr.write("\n")
    sys.stderr.write("\nStart to setup webpage\n")
    ip = sys.argv[1]
    keyfile = 'assignment6.pem'
    keypath = '/home/npc/'
    init_web(ip, keyfile, keypath)
    sys.stderr.write("\nFinish setting up webpage\n")
    exit(0)
