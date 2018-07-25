Do you always have to create your vpn account after few days?

Here is a solution, this is a script that will auto renew your vpn account.

You will need mechanize library of python. If you dont have this install this library .You can do this by using pip.

     pip install mechanize
or

     sudo pip install mechanize
For this you will have to first set up your vpn settings in network settings.You will have to do this only for the first time.

If you have already done this settings then skip to step-3.

Step 1- Download the configuration file for india2 sserver from this url. http://www.vpnjantit.com/assets/in2.vpnjantit.com.zip

Step 2- Open settings and add this configuration file.(use port 443 for IITG proxy).

step 3- Downlaod the repo files.

step 4- Place both files in same directory. vpn.py and cronscript.py

step 5- Now open vpn.py file and edit the username and password variable according to your choice of username and password.

Step 6- open terminal in this directory.

step 7- Run cronscript.py. Type the below command in terminal.

    python cronscript.py
*Enter the info as per asked.

*Don't forget to enter full path when asked .Check for "vpn.py" at the end of the path.

step 8- A txt file with name cron_list.txt will be generated in the same directory.Now open it and copy all the lines inside it.

step 9- Type the below command in the terminal (if you are writing this command for first time ,you will be asked about your
choice of editor ,select any editor of your choice.)

    sudo crontab -e
step 10- Paste the copied lines at end of this file which just opened and save the file .

Finally you are done ,now your vpn account will get auto renewed after seven days.
