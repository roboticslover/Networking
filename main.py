import streamlit as st
import requests

# Function to find data scientists based on location using GitHub API


def find_data_scientists(location, job_role):
    url = 'https://api.github.com/search/users'
    params = {
        'q': f'location:{location} language:python data science {job_role}',
        'per_page': 100,  # Adjust the number of results as needed
    }
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        # Add your GitHub API token if needed
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        if response.status_code == 200:
            data = response.json()
            # Return a list of data science-related users
            return data.get('items', [])
        else:
            st.error(
                f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.RequestException as e:
        st.error(f"Error occurred: {e}")

    return []


def main():
    st.title("Find Data Scientists")
    st.write("Let's find data scientists based on location and job role.")

    # Add a text input for users to enter the country name
    country = st.text_input("Enter Country Name:", "")

    # Dictionary of job roles with their corresponding keywords
    job_roles = {
        "Data Scientist": "data science",
        "Data Analyst": "data analysis",
        "Machine Learning Engineer": "machine learning",
        # Add more job roles and keywords as needed
    }

    if country.strip() != "":
        # Suggest specific areas or cities within the country
        areas = get_areas(country)
        if areas:
            area = st.selectbox("Select Area/City:", areas)
            if area:
                job_role = st.selectbox(
                    "Select Job Role:", list(job_roles.keys()))
                if st.button("Find"):
                    # Call the function to find data scientists in the specified location and job role
                    data_scientists = find_data_scientists(
                        area, job_roles[job_role])
                    if data_scientists:
                        st.header(f"{job_role}s in {area}")
                        for scientist in data_scientists:
                            st.write(
                                f"- {scientist['login']} ({scientist['html_url']})")
                    else:
                        st.write(f"No {job_role}s found in {area}.")
        else:
            st.warning(
                f"No areas/cities found in {country}. Please enter a different country.")


def get_areas(country):
    # Function to get areas or cities within the specified country (dummy implementation)
    # Replace this with your actual implementation using APIs or datasets
    if country.lower() == "1":
        return ["USA", "UK", "Canada", "Israel"]
    elif country.lower() == "2":
        return ["Germany", "France", "Italy", "Denmark"]
    elif country.lower() == "3":
        return ["Switzerland", "Netherlands", "Sweden", "Finland"]
    elif country.lower() == "4":
        return ["Australia", "Belgium", "Norway", "Dubai"]
    elif country.lower() == "5":
        return ["Japan", "Korea", "Singapore", "Hong Kong"]
    elif country.lower() == "6":
        return ["San Francisco", "New York", "Seattle", "Austin"]
    elif country.lower() == "7":
        return ["Denver", "Boston", "Chicago", "Raleigh"]
    elif country.lower() == "8":
        return ["Bangalore", "Hyderabad", "Pune", "Mumbai"]
    elif country.lower() == "9":
        return ["Delhi", "Chennai", "Ahmedabad", "Jaipur"]
    # Add more countries and their areas/cities as needed
    else:
        return []


if __name__ == "__main__":
    main()
