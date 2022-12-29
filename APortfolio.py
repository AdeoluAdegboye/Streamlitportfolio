from modulefinder import Module
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import requests
from streamlit_option_menu import option_menu



# st.set_page_config(layout="wide") 
# [theme]
base="light"
# My BackgroundColor= "#OB1A39"


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #ED46D1;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  #put logo image
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.title("        Hi I am Adeolu Adegboye ")

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions -add more columns to the table
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

# MAIN 

def main():
	"""OPtions menu """
	
	choice = option_menu(
			menu_title =None, 
			options = ["About Me","My Projects","Contact Me"], 
			icons = ["house", "books", "envelope"],
			menu_icon="cast", 
			default_index=0,
			orientation= "horizontal",
			)
	
	if choice == "About Me":
		image = Image.open('aboutme.jpg')
		st.image(image, width = 1350)
		
		st.title("Here is a Summary of My Work and Skills")
				# st.sidebar.selectbox("Menu",menu)

		# st.subheader("")
		photo = Image.open('Homepage1.jpg')
		st.image(photo, width = 1350)
		st.write('')

	elif choice == "My Projects":
		st.title("Data analysis and machine learning projects I have done")
		st.write("Detals to these projects can be found on My Github Portfolio [here](https://github.com/AdeoluAdegboye)")
        
		photo = Image.open('myprojects.jpg')
		st.image(photo, width = 1350)
                 
		st.write("Here's my medium article on a project where I and a team analyzed water bodies to determine their suitability for solar panel [installment](https://medium.com/thebaselineblog/a-technical-case-study-on-the-preprocessing-and-modeling-phases-of-an-aquatic-solar-site-eda539a9793d)")
		# st.subheader(" User Login ")

	elif choice == "Contact Me":
		photo = Image.open('contact.jpg')
		st.image(photo, width = 1350)
		
		# st.subheader("Create New Account")
		# new_user = st.text_input("Username")
		# new_password = st.text_input("Password",type='password')

		# if st.button("Signup"):
		# 	create_usertable()
		# 	add_userdata(new_user,make_hashes(new_password))
		# 	st.success("You have successfully created a valid Account")
		# 	st.info("Go to Login Menu to login")





if __name__ == '__main__':
	main()
