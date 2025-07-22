import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("User Management Dashboard")

# View all users
if st.button("Load Users"):
    response = requests.get(f"{API_URL}/")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            st.write(f"ID: {user['id']} | Name: {user['name']} | Age: {user['age']}")
    else:
        st.error("Failed to load users.")

# Add user
st.subheader("Add New User")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, step=1)

if st.button("Add User"):
    if name.strip() == "":
        st.warning("Name cannot be empty.")
    else:
        payload = {"name": name, "age": age}
        response = requests.post(f"{API_URL}/users", json=payload)
        if response.status_code == 201:
            st.success("User added successfully")
        else:
            st.error("Failed to add user.")

# Delete user by ID
st.subheader("Delete User by ID")
delete_id = st.number_input("User ID to delete", min_value=1, step=1)

if st.button("Delete User"):
    response = requests.delete(f"{API_URL}/users/{int(delete_id)}")
    if response.status_code == 200:
        st.success(f"User {int(delete_id)} deleted successfully")
    else:
        st.error("Failed to delete user")
