#### Installing Jenkins on Ubuntu
__[Jenkins wiki](https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Ubuntu)__

##### Installation

    wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins

##### Upgrade
*   Once installed as above, update to the later version of Jenkins (when it comes out)
    can be done by running the following commands:


    sudo apt-get update
    sudo apt-get install jenkins
    

* `jenkins` user is created to run this service.
* Log file will be placed in `/var/log/jenkins/jenkins.log`.
* configuration parameters for the launch `/etc/default/jenkins`
* Home directory for the Jenkins is `/var/lib/jenkins`
* service status check : `service jenkins status`
* Checkout source codes are stored at `/var/lib/jenkins/workspace/`
* Public and private keys are stored at `/var/lib/jenkins/.ssh/`    
* Start up
    

    There is a jenkins startup script placed at `/etc/init.d/jenkins` after installation of the package.
    This makes jenkins server up and running after each reboot.

#### User/admin password
* User password is stored at `/var/lib/jenkins/users/<admin>/config.xml`
* A hashed password is stored for tag 'passwordHash'


    A test password with hash value `#jbcrypt:$2a$10$razd3L1aXndFfBNHO95aj.IVrFydsxkcQCcLmujmFQzll3hcUrY7S` can be used to
set the password to 'test' when password is lost.

### Error:
* hudson.plugins.git.GitException: Command "git fetch....returned status code 128:
  Host key verification failed.
    
    * [X] Check if /var/libs/jenkins/.ssh contains `id_rsa`, `id_rsa.pub` and `known_hosts`
    * [X] Check is `jenkins` user is the owner of those files
    * [X] The git server should be added to the list of known_host (May be done using below step) 
    * [X] Check if connection to Git server is possbile from the command line with-in the `jenkins` user terminal
    
    
* Proxy related error while installing external plug-in
    * [X] Jenkins ->Plugin Manager->HTTP Proxy Configuration
    * [X] Server: Give numeric value of IP
    * [X] Port, Username, password to access the Proxy Server.
     
##### Repo Access Error:

    Failed to connect to repository : Command "git ls-remote -h ssh://git@gitserver:/opt/git/hello-world.git HEAD" returned status code 128:
    stdout:
    stderr: Host key verification failed.
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.

To resolve this error (if you think all other settings are correct then..):

    Run the command `git ls-remote -h ssh://git@gitserver:/opt/git/hello-world.git` from local terminal and
    give `yes` to the ECDSA key fingerprint is... question that pops up while connecting to a new unauthenticated Host.

Sometimes `Credentials` is needed to have Jenkins access the git repo.
It can be found in the `Repository URL` section!


###### Steps to find the proxy server IP address, can be looked at __[proxy info](https://github.com/Kalinga/linuxHelper/blob/master/proxy/proxy.md)__

#### email setup with Jenkins

* [X] Manage Jenkins->Configure System->E-mail Notification
* [X] Fill the data for SMTP server (Check Below steps how to find it)

    
    ctrl + r
    nslookup
    set type=all
    _ldap.tcp.dc._msdcs.<domain>
    check the output under 'Non-authoritative answer:'
    

    