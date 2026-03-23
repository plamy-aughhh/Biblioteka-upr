import streamlit as st
books = [ "The Hobbit", "1984", "Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby" ]
st.title("Library")
st.write("Enter a book title to see if it exists in the database")
user_input = st.text_input ("Book Title")

if st.button("Check Box"):
  if user_input.strip() == "":
    st.warning("Please enter a book title")
  elif user_input in books:
    st.success("The book is in the database! ")
  else:
    st.error("The book is not in  the database. ")
    user_input = st.text_input("Add a book")
    if st.button("Add"):
      user_input = {
        "title": new_book
      }
      st.books.append(user_input)
      st.success("The book was added to the database! ")
      if len(st.books.append) == 0:
        st.write("There are no new added books")
      else:
        for user_input in books:
          st.write(book["title"])
        
