training = """I do not expect Blowfish to return string in a given format. I expect that it will be random. By saying, that human input can be random I meant, that it can be one word, several words, orOneWordCreatedFromSeveralWords. This method has to tell me, if input is clearly a random string (e.g. "edgyewfduysfd") or something "humanish" (e.g. "BusinessLogicCoreClass"). So that's why my first gues was to check normal distribution of input string. – user2265495
May 8, 2013 at 11:40
And I will say this again: this method doesn't have to be an oracle, 80% of accuracy will be enaugh :) (its result will be only a hint) – user2265495
May 8, 2013 at 11:41
@user2265495 80% accuracy; check for word length, assuming the algorithm even puts spaces in then they'll occure 1 in 27 times, whereas I'd expect english language to be 1 in 5 or 6. One word: less that 20% of time probably, many words without spaces: how often does that happen – 
Richard Tingle
May 8, 2013 at 11:45
@Richard - unfortunatly, many words without spaces could happen frequently in this case, because this KNIME node will encrypt and decrypt class names (among other stuff). So strings like "BusinessLogicCoreClass" will be quite normal input for this node. – user2265495
May 8, 2013 at 11:53
@user2265495: "This method has to tell me, if input is clearly a random string (e.g. "edgyewfduysfd") or something "humanish" (e.g. "BusinessLogicCoreClass")" Then you have to calculate its entropy, but again, my point is that a human can provide a string which is random enough to fool this method (the shorter the string, the more probable the fooling). Probably Richard's answer is the closest you can get. – 
m0skit0
May 8, 2013 at 12:41

Skip to content

    opsdisk
    /
    the_cyber_plumbers_handbook

Code
Issues 4
Pull requests
Actions
Projects
Security

    Insights

Owner avatar
the_cyber_plumbers_handbook
Public

opsdisk/the_cyber_plumbers_handbook
2 branches
0 tags
Latest commit
@opsdisk
opsdisk Merge pull request #1 from opsdisk/add-student-discount-info
bf9213e
Oct 27, 2021
Git stats

    3 commits

Files
Type
Name
Latest commit message
Commit time
img
Initial commit
September 6, 2021 14:44
LICENSE.md
Initial commit
September 6, 2021 14:44
README.md
Updated README with student discount info.
October 27, 2021 08:21
cph_version_1.4_20210829.pdf
Initial commit
September 6, 2021 14:44
README.md

The Cyber Plumber's Handbook

This repo contains the PDF book The Cyber Plumber's Handbook - The definitive guide to Secure Shell (SSH) tunneling, port redirection, and bending traffic like a boss. The book was first published in October 2018 for purchase, but now I'm providing it for FREE to anyone interested in learning more about the magic of SSH tunnels and port redirection.
Book Overview

This book is packed with practical and real world examples of SSH tunneling and port redirection in multiple realistic scenarios. It walks you through the basics of SSH tunneling (both local and remote port forwards), SOCKS proxies, port redirection, and how to utilize them with other tools like proxychains, nmap, Metasploit, and web browsers.

Advanced topics included SSHing through 4 jump boxes, throwing exploits through SSH tunnels, scanning assets using proxychains and Metasploit's Meterpreter, browsing the Internet through a SOCKS proxy, utilizing proxychains and nmap to scan targets, and leveraging Metasploit's Meterpreter portfwd command.
Getting Started

    Agree to the terms of the Creative Commons Attribution-NonCommercial 4.0 International License which is also outlined here.

    Download the latest PDF from here.

    Purchase the The Cyber Plumber's Lab Guide and Interactive Access from here. Your purchase includes a PDF lab guide with 45+ exercises and 28 days of interactive access to a real live lab to practice SSH tunneling and port redirection techniques!

Interactive Lab

The Cyber Plumber's Lab Guide and Interactive Access can be purchased here. There is a 75% off discount for students...just send an email to cph-student@opsdisk.com from your educational email address.
Why purchase?

SSH tunneling is a skill you can use for the rest of your IT career! SSH tunneling and port redirection are skills that can be applied in any information technology discipline, so it does not matter if you are a network engineer, red teamer, penetration tester, developer, or something in between. That being said, the examples tend to skew towards pairing tunneling techniques with penetration testing tools.

Lab Description

Four jump boxes provide the Internet facing portion of the lab. However, the fun really starts when you start leveraging tunneling techniques to reach the internal side of the network to access services such as Secure SHell (SSH), Web, and Remote Desktop Protocol (RDP). The Linux and Windows targets are also running vulnerable services that can be exploited for the true tunneling ninjas. Each of the exercises has a brief description and solution to assist you in the event you get stuck.

Requirements

The interactive lab portion requires a Linux-based host or virtual machine (preferably Kali), Internet access, a basic grasp of networking and Information Technology fundamentals, and Linux commands. The use of a Windows Operating System to access the lab has not been tested. Immediately after purchasing this, you will receive an SSH private key via email and instructions on how to access the lab. Your lab time starts immediately after purchasing, so plan accordingly!
Testimonial

    After your course, I have been able to:

        Stand-up a cloud-hosted Kali box, configure OpenVAS, ssh into the box...all encrypted yet run on my local browser. I no longer have to bother with installing VNC.

        Same thing with Dradis...allows a penetration testing team to collaborate on an assignment without having to mess with certificates.

        I wrote a script that launches 10 VMs in DigitalOcean in seconds, then I ssh into them with -D 9050...9059. I have 10 entries in my proxychains.conf file for 127.0.0.1 9050...127.0.0.1 9059, and then launch theHarvester with proxychains. Google no longer accuses me of being a bot.

        I passed a tip along to a network engineer at my company that he should read your book rather than exposing an administrative login page on a public facing website.

        For privacy, I sometimes create a VM on the fly and use it as a proxy in Firefox."

Bulk / Team Pricing

The purchase of the lab guide and access is for individual use only. If you are interested in bulk or team pricing for your organization, please contact me using here. Access keys cannot be shared and your lab access will be immediately revoked without a refund if you are discovered doing this.
FAQ

    What if I find a error / typo?

    Submit a issue here

    Will you open source the LaTeX files?

    Maybe

Contact

    Email
    @opsdisk

License

Distributed under the Creative Commons Attribution-NonCommercial 4.0 International License. See LICENSE.md for more information.

Creative Commons License
This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
About

Free copy of The Cyber Plumber's Handbook
Topics
ssh socks5 penetration-testing tunneling proxychains kali blueteam pivoting oscp redteam lateral-movement
Resources
Readme
License
View license
Activity
Stars
2.3k stars
Watchers
35 watching
Forks
151 forks
Report repository
Releases
No releases published
Footer
© 2023 GitHub, Inc.
Footer navigation

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Main menu

Wikipedia The Free Encyclopedia

    Create account
    Log in

Personal tools

Contents
(Top)

"""
import numpy as np

def get_dict(x):
    x = x.lower()
    N = len(x)-1
    d = {"smallest":1/N}
    for i in range(len(x)-1):
        try:
            d[x[i:i+2]] +=1/N
        except:
            d[x[i:i+2]] = 1/N
    
    return d

def H(x,d):
    ent = 0
    for i in range(len(x)-1):
        try:
            p = d[x[i:i+2]]*1
            ent-= p*np.log(p)
        except:
            p = d["smallest"]
            ent-=p*np.log(p)
    return ent/(len(x)-1)


D = get_dict(training)

def probably_human_written(x):
    entropy = H(x,D)
    if entropy>0.015:
        return True
    else:
        return False



print(probably_human_written("qwert yui oasdfsaf asfasf jlkjxz lcjkv pasd fghjklzxc vbnm"))
print(probably_human_written("hallo ik ben leander post en ik woon in utrecht"))
