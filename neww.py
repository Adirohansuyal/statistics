import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("CSV Data Analysis and Visualization")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.subheader("Data Preview")
    st.write(df.head())

    # Show basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Select a column to filter the data
    column_to_filter = st.selectbox("Select a column to filter", df.columns)
    unique_values = df[column_to_filter].unique()
    selected_value = st.selectbox(f"Select a value from {column_to_filter}", unique_values)

    # Filter the data
    filtered_df = df[df[column_to_filter] == selected_value]
    st.subheader(f"Filtered Data by {column_to_filter}: {selected_value}")
    st.write(filtered_df)

    # Display a bar chart based on the filtered data
    st.subheader("Bar Chart of the Filtered Data")
    # Let's assume we want to visualize a numeric column in a bar chart
    numeric_columns = filtered_df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        column_to_plot = st.selectbox("Select a numeric column for the bar chart", numeric_columns)
        fig, ax = plt.subplots()
        sns.barplot(x=filtered_df[column_to_filter], y=filtered_df[column_to_plot], ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available to plot.")
