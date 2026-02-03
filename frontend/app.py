'''
import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI-HCP CRM", layout="wide")
st.title("💊 AI-HCP CRM Dashboard")

menu = ["Home", "HCPs", "Interactions"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- HOME ----------------- #
if choice == "Home":
    st.subheader("Welcome to AI-HCP CRM")
    st.write("Use the sidebar to navigate between HCPs and Interactions.")

# ----------------- HCPs ----------------- #
elif choice == "HCPs":
    st.subheader("👨‍⚕️ HCP Management")

    action = st.radio("Choose Action", ["View HCPs", "Add New HCP", "View HCP History"])

    if action == "View HCPs":
        try:
            response = requests.get(f"{BASE_URL}/hcp/")
            hcps = response.json()
            if hcps:
                for hcp in hcps:
                    st.write(f"**{hcp['name']}** ({hcp['specialty']}) - {hcp['hospital']}, {hcp['city']}")
                    st.write(f"📞 {hcp['phone']} | ✉️ {hcp['email']}")
                    st.markdown("---")
            else:
                st.info("No HCPs found.")
        except Exception as e:
            st.error(f"Error fetching HCPs: {e}")

    elif action == "Add New HCP":
        st.write("### Add New HCP")
        with st.form(key="add_hcp"):
            name = st.text_input("Name")
            hospital = st.text_input("Hospital")
            specialty = st.text_input("Specialty")
            city = st.text_input("City")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submit = st.form_submit_button("Add HCP")

        if submit:
            payload = {
                "name": name,
                "hospital": hospital,
                "specialty": specialty,
                "city": city,
                "phone": phone,
                "email": email
            }
            try:
                resp = requests.post(f"{BASE_URL}/hcp/", json=payload)
                if resp.status_code == 200:
                    st.success(f"HCP '{name}' added successfully!")
                else:
                    st.error(f"Failed to add HCP: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif action == "View HCP History":
        st.write("### HCP Interaction History")
        hcp_id = st.number_input("Enter HCP ID", min_value=1, step=1)
        if st.button("Fetch History"):
            try:
                resp = requests.get(f"{BASE_URL}/hcp/{hcp_id}/history")
                if resp.status_code == 200:
                    history = resp.json()
                    for h in history:
                        st.write(f"**Interaction ID:** {h['id']}")
                        st.write(f"**Raw Text:** {h['raw_text']}")
                        st.write(f"**Summary:** {h['summary']}")
                        st.write(f"**Sentiment:** {h['sentiment']}")
                        st.write(f"**Follow-up:** {h['follow_up']}")
                        st.write(f"**Created At:** {h['created_at']}")
                        st.markdown("---")
                else:
                    st.warning("No history found or invalid HCP ID.")
            except Exception as e:
                st.error(f"Error: {e}")

# ----------------- INTERACTIONS ----------------- #
elif choice == "Interactions":
    st.subheader("📝 Interactions")

    action = st.radio("Choose Action", ["Log Interaction", "View All Interactions", "Edit Interaction"])

    if action == "Log Interaction":
        with st.form(key="log_interaction"):
            hcp_id = st.number_input("HCP ID", min_value=1, step=1)
            raw_text = st.text_area("Interaction Details")
            follow_up = st.text_area("Follow-up Action")
            submit = st.form_submit_button("Log Interaction")

        if submit:
            payload = {"hcp_id": hcp_id, "raw_text": raw_text, "follow_up": follow_up}
            try:
                resp = requests.post(f"{BASE_URL}/interactions/log", json=payload)
                if resp.status_code == 200:
                    st.success("Interaction logged successfully!")
                    st.json(resp.json())
                else:
                    st.error(f"Failed to log interaction: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif action == "View All Interactions":
        try:
            resp = requests.get(f"{BASE_URL}/interactions/")
            if resp.status_code == 200:
                interactions = resp.json()
                for i in interactions:
                    st.write(f"**ID:** {i['id']} | **HCP ID:** {i['hcp_id']} | **Sentiment:** {i['sentiment']}")
                    st.write(f"**Raw Text:** {i['raw_text']}")
                    st.write(f"**Summary:** {i['summary']}")
                    st.write(f"**Follow-up:** {i['follow_up']}")
                    st.write(f"**Created At:** {i['created_at']}")
                    st.markdown("---")
            else:
                st.info("No interactions found.")
        except Exception as e:
            st.error(f"Error: {e}")

    elif action == "Edit Interaction":
        with st.form(key="edit_interaction"):
            interaction_id = st.number_input("Interaction ID", min_value=1, step=1)
            raw_text = st.text_area("Updated Interaction Details")
            follow_up = st.text_area("Updated Follow-up Action")
            submit = st.form_submit_button("Update Interaction")

        if submit:
            payload = {"raw_text": raw_text, "follow_up": follow_up}
            try:
                resp = requests.put(f"{BASE_URL}/interactions/edit/{interaction_id}", json=payload)
                if resp.status_code == 200:
                    st.success("Interaction updated successfully!")
                    st.json(resp.json())
                else:
                    st.error(f"Failed to update interaction: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")
'''

import streamlit as st
import requests
import pandas as pd

# ---------------- CONFIG ---------------- #
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Medicine World CRM",
    page_icon="💊",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("Medicine World CRM")
menu = ["Dashboard", "HCPs", "Interactions"]
choice = st.sidebar.radio("Navigation", menu)

# ---------------- DASHBOARD ---------------- #
if choice == "Dashboard":
    st.markdown("<h2 style='text-align: center;'>💊 Medicine World CRM Dashboard</h2>", unsafe_allow_html=True)
    st.write("Welcome to the CRM system for Healthcare Professionals. Use the sidebar to navigate.")

    # Quick Stats
    try:
        hcps = requests.get(f"{BASE_URL}/hcp/").json()
        interactions = requests.get(f"{BASE_URL}/interactions/").json()
        col1, col2 = st.columns(2)
        col1.metric("Total HCPs", len(hcps))
        col2.metric("Total Interactions", len(interactions))
    except:
        st.warning("Backend server not reachable!")

# ---------------- HCPs ---------------- #
elif choice == "HCPs":
    st.header("👨‍⚕️ Healthcare Professionals (HCPs)")

    action = st.selectbox("Select Action", ["View All HCPs", "Add New HCP", "View HCP History"])

    if action == "View All HCPs":
        try:
            hcps = requests.get(f"{BASE_URL}/hcp/").json()
            if hcps:
                df = pd.DataFrame(hcps)
                st.dataframe(df[['id','name','specialty','hospital','city','phone','email']])
            else:
                st.info("No HCPs found.")
        except Exception as e:
            st.error(f"Error fetching HCPs: {e}")

    elif action == "Add New HCP":
        st.subheader("➕ Add New HCP")
        with st.form(key="add_hcp_form"):
            name = st.text_input("Name")
            hospital = st.text_input("Hospital")
            specialty = st.text_input("Specialty")
            city = st.text_input("City")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submit = st.form_submit_button("Add HCP")
        if submit:
            payload = {"name": name, "hospital": hospital, "specialty": specialty, "city": city, "phone": phone, "email": email}
            try:
                resp = requests.post(f"{BASE_URL}/hcp/", json=payload)
                if resp.status_code == 200:
                    st.success(f"HCP '{name}' added successfully!")
                else:
                    st.error(f"Failed to add HCP: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif action == "View HCP History":
        st.subheader("📜 HCP Interaction History")
        hcp_id = st.number_input("Enter HCP ID", min_value=1, step=1)
        if st.button("Fetch History"):
            try:
                resp = requests.get(f"{BASE_URL}/hcp/{hcp_id}/history")
                if resp.status_code == 200:
                    history = resp.json()
                    if history:
                        for h in history:
                            st.markdown(f"### Interaction ID: {h['id']}")
                            st.write(f"**HCP ID:** {h['hcp_id']}")
                            st.write(f"**Raw Text:** {h['raw_text']}")
                            st.write(f"**Summary:** {h['summary']}")
                            st.write(f"**Sentiment:** {h['sentiment']}")
                            st.write(f"**Follow-up:** {h['follow_up']}")
                            st.write(f"**Created At:** {h['created_at']}")
                            st.markdown("---")
                    else:
                        st.info("No interactions found for this HCP.")
                else:
                    st.error("Invalid HCP ID or server error.")
            except Exception as e:
                st.error(f"Error: {e}")

# ---------------- INTERACTIONS ---------------- #
elif choice == "Interactions":
    st.header("📝 Interactions Management")

    action = st.selectbox("Select Action", ["Log Interaction", "View All Interactions", "Edit Interaction"])

    if action == "Log Interaction":
        st.subheader("🖊 Log New Interaction")
        with st.form(key="log_interaction_form"):
            hcp_id = st.number_input("HCP ID", min_value=1, step=1)
            raw_text = st.text_area("Interaction Details")
            follow_up = st.text_area("Follow-up Action")
            submit = st.form_submit_button("Log Interaction")
        if submit:
            payload = {"hcp_id": hcp_id, "raw_text": raw_text, "follow_up": follow_up}
            try:
                resp = requests.post(f"{BASE_URL}/interactions/log", json=payload)
                if resp.status_code == 200:
                    st.success("Interaction logged successfully!")
                    st.json(resp.json())
                else:
                    st.error(f"Failed to log interaction: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif action == "View All Interactions":
        st.subheader("📋 All Interactions")
        try:
            interactions = requests.get(f"{BASE_URL}/interactions/").json()
            if interactions:
                df = pd.DataFrame(interactions)
                st.dataframe(df[['id','hcp_id','raw_text','summary','sentiment','follow_up','created_at']])
            else:
                st.info("No interactions found.")
        except Exception as e:
            st.error(f"Error fetching interactions: {e}")

    elif action == "Edit Interaction":
        st.subheader("✏️ Edit Interaction")
        with st.form(key="edit_interaction_form"):
            interaction_id = st.number_input("Interaction ID", min_value=1, step=1)
            raw_text = st.text_area("Updated Interaction Details")
            follow_up = st.text_area("Updated Follow-up Action")
            submit = st.form_submit_button("Update Interaction")
        if submit:
            payload = {"raw_text": raw_text, "follow_up": follow_up}
            try:
                resp = requests.put(f"{BASE_URL}/interactions/edit/{interaction_id}", json=payload)
                if resp.status_code == 200:
                    st.success("Interaction updated successfully!")
                    st.json(resp.json())
                else:
                    st.error(f"Failed to update interaction: {resp.text}")
            except Exception as e:
                st.error(f"Error: {e}")
