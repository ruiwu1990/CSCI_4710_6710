This project is a coding convention checking tool. Here are the rules and library used:
<!-- # checking coding convention
pylint
cppcheck -->

* Python: rule-[PEP8](https://www.python.org/dev/peps/pep-0008/) lib-[pylint](https://www.pylint.org/#install).
* Java: rule-[Sun](https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/sun_checks.xml) or [Google]-(https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml), Sub is used as default, lib-[checkstyle](http://checkstyle.sourceforge.net/cmdline.html#Download_and_Run)

The above code checkers should be installed before the app is set up.

Our project also uses [codemirror](https://codemirror.net/) to display codes on the webpage.
## Quick Start
### Local Test Setup
To fufil all the requirements for the python server, you need to run:
```
sudo pip3 install -r requirements.txt
```

### Docker Setup
You can run the program by:
```
docker run --name <container_name> -h <IP> -p 5000:5000 ruiwu1990/coding_convention_tool python cct_main.py
```

<IP> should be replaced with your machine ip address. The command is to set up a server with your machine
-p 5000:5000 means that mapping host machine port 5000 (first one) with docker container port 5000 (second one).
Here is the command that I used:

```
docker run --name tmp2 -h 150.216.57.36 -p 5000:5000 ruiwu1990/coding_convention_tool python cct_main.py
```

