import streamlit as st
st.title ("Библиотека с книги")
books = [ "The Hobbit", "1984", "Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby" ]
st.title("Book checker app")
st.write("Enter a book title to see if it exists in the database")
user_input = st.text_input ("Book Title")

if st.button("Check Box"):
  if user_input.strip() == "":
    st.warning("Please enter a book title")
  elif user_input in books:
    st.success("The book is in the database! ")
  else:
    st.error("The book is not in  the database. ")
    new_book = st.text_input("Add a book")
    if st.button("Add"):
    st.write(new_book) 
