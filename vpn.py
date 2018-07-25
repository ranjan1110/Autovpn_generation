#!/usr/bin/env/python
#edit username and password according to your choice
username="username"
password="pass"
import mechanize 

br = mechanize.Browser() 

br.set_handle_robots(False)

br.addheaders = [("User-agent","Mozilla/5.0")]



india=br.open("http://www.vpnjantit.com/create-free-account.html?type=OpenVPN&server=India2")


br.select_form(action='create-free-account.html?type=OpenVPN&server=India2')
br["user"] = username
br["pass"]=password
response = br.submit()
