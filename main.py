#!/usr/bin/env python3

import subprocess, os, time

workingDir = os.getcwd() # get current working directory


print("\n\nEnter the following:")
firstName_whoami = raw_input("First Name: ")
lastName_whoami = raw_input("Last Name: ")
email_whoami = raw_input("Email: ")

subprocess.call("bzr whoami \"{0} {1} <{2}>\"".format(firstName_whoami, lastName_whoami, email_whoami), shell=True)

bzr_login = raw_input("Do you want to enter your Launchpad login and ID "
    "(this way code that you publish in Launchpad will be associated with you)? [Y/N] ")
bzr_login.lower()
                                                                
if bzr_login == "y":
    launchpad_login = raw_input("Launchpad login: ")
    launchpad_id = raw_input("Launchpad ID: ")
    subprocess.call("bzr {0} {1}".format(launchpad_login, launchpad_id), shell=True)
else:
    pass

print("\nIMPORTANT: Do NOT use uppercase characters for your project name or project folder url. Otherise your program won't compile!")
project_name = raw_input("\n\nEnter the name of your program (which should be the same as your project folder name): ")
directory = raw_input("Enter the url of your project folder: ")

subprocess.call("tar zcf {0}.tar.gz -C {1}".format(project_name, directory, shell=True)) # compress project into a tar.gz file
subprocess.call("cd {0}".format(dir), shell=True) # move into the project directory
subprocess.call("bzr dh-make ../{0} 1.0 ../{1}.tar.gz".format(project_name, project_name), shell=True)
subprocess.call("cd {0}/debian && rm *ex *EX && cd -".format(project_name), shell=True) # remove unessecary file from "debian" directory

print("\nFill in the following: ")
homepage = raw_input("Homepage(optional): ")
maintainer_name = raw_input("(company) name: ")
maintainer_email = raw_input("(company) email: ")
maintainer_email = "<" + maintainer_email + ">"
short_summary = raw_input("Short summary (max 60 characters): ")
long_description = raw_input("Long description: ")

depend_choice = raw_input("\nDoes your program have any dependencies? [Y/N] ")
depend_choice.lower()
if depend_choice == 'y':
    dependencies = raw_input("Enter each dependency, separated by a comma:")
else:
    pass

with open("control", "a") as f:
    control = ["Source: ",
               "\nSection: {}".format(project_name),
               "\nPriority: optional",
               "\nMaintainer: {0} {1}".format(maintainer_name, maintainer_email),
               "\nStandards-Version: ",
               "\nBuild-Depends: ",
               "\nHomepage: {}".format(homepage),
               "\n\nPackage: {}".format(project_name),
               "\nArchitecture: any",
               "\nDepends: {}".format(dependencies),
               "\nDescription: {}".format(short_summary),
               "\n\t {}".format(long_description)]
    f.writelines(control)

subprocess.call("bzr add debian/source/format && bzr commit -m \"Initial commit of Debian packaging.\"", shell=True)
subprocess.call("bzr builddeb -- -us -uc", shell=True)
subprocess.call("ls")
