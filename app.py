import streamlit as st
st.title ("Списък със спортисти от България")
ppl = [ "Филип Буков", "Красимир Костадинов", "", "
Любомир Палакарчев", "Иван Селвелиев" ]
st.title("Спорт в България")
st.write("Въведи името на спортист и провери дали е в списъка")
user_input = st.text_input ("Име")

if st.button("Check Box"):
  if user_input.strip() == "":
    st.warning("Please enter a book title")
  elif user_input in ppl:
    st.success("The book is in the database! ")
  else:
    st.error("The book is not in  the database. ")
    new_pers = st.text_input("Add a book")
    if st.button("Add"):
      st.write(new_pers)
      
