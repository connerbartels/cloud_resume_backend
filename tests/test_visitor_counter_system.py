import requests
import pytest

# Define the API endpoint URL
API_URL = 'https://godg5nr2z4.execute-api.us-east-1.amazonaws.com/visitorCounter'

def test_visitor_counter_system():
    """
    Add docstring for test_visitor_counter_system
    """

    # Make the first request to get the initial visitor count
    print("\nMaking the first request to get the initial visitor count")
    response = requests.get(API_URL)
    
    # Check the response status code
    print(f"Checking if the response status code is 200. Status code received: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
    

    # Check if the response contains a valid integer for visitor count
    print(f"Checking if the response contains a valid visitor count")
    try:
        initial_count = int(response.text.strip())
        print(f"Initial visitor count retrieved: {initial_count}")
    except ValueError:
        pytest.fail(f"Visitor count is missing or not a valid integer. Response body: '{response.text}'")
    
    # Verify the CORS header (Access-Control-Allow-Origin)
    cors_header = response.headers.get('Access-Control-Allow-Origin')
    print(f"Verifying the CORS header. CORS header value: {cors_header}")
    # Add assertion
    
    # Make the second request to increment the visitor count
    print("Making the second request to increment the visitor count")
    response = requests.get(API_URL)
    
    # Check the status code again
    print(f"Checking if the response status code is 200 again. Status code received: {response.status_code}")
    # Add assertion
    
    # Ensure the visitor count has incremented by 1
    updated_count = int(response.text.strip())
    print(f"Updated visitor count retrieved: {updated_count}")
    # Add assertion
    
    # Print success message for debugging purposes
    print(f"Test passed: Visitor count incremented from {initial_count} to {updated_count}")
