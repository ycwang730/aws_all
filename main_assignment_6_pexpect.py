import pexpect
import main_assignment_6
from main_assignment_6 import *
dir(main_assignment_6)


print dns_name

os.system('ssh -i "assignment6.pem" ec2-user@%s' %dns_name)
#child = pexpect.spawn("ssh ec2-user@%s" % dns_name)
#child.expect('(yes/no)?')
#child.sendline('yes')
