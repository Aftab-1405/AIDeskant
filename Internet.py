import wikipedia
import webbrowser
import requests
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# This is a function that checks internet connection.


def check_internet_connection():
    """
    Check if internet connection is available by sending a GET request to Google.

    Returns:
    True if internet connection is available, False otherwise.
    """
    try:
        # Send a GET request to Google
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        # Connection error, internet is not available
        return False
    except requests.Timeout:
        # Timeout error, internet is slow or unresponsive
        return False


# print(check_internet_connection()) # Checks only returned value of this function, which is in boolean form.

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# This function will get executed If rake is not able to found answer from its database. And will try to search on wikipedia.

def check_on_wikipedia(query):
    try:
        # Use the query directly without unnecessary modifications
        data = wikipedia.summary(query, sentences=3)
        return data
    except Exception as e:
        return ""

# This function can direcly search queries on default browser of the system.


def web_search(query):
    if query.lower().startswith("google"):
        query = query[6:].strip()
    elif query.lower().startswith("search for"):
        query = query[10:].strip()
    # Replace spaces with plus signs to create a valid URL
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    # Open the URL in the default web browser
    webbrowser.open(url)
    return "Searching on Google for " + query + "..."

# The function below uses api key and search engine id. Both of which i got by creating my own search engine using my gamil, which has name as "Aftab Custome Search".


# def search_on_google(query):
#     if query.lower().startswith("google"):
#         query = query[6:].strip()
#     elif query.lower().startswith("search for"):
#         query = query[10:].strip()

#     # Set up the Google Custom Search API request
#     api_key = "AIzaSyCOKkruMJU-wZLeTp9aGir375uFd-oywg8"
#     cx = "b3fa7d955dd604a98"
#     url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"

#     try:
#         # Send the API request and retrieve the search results
#         response = requests.get(url)
#         data = response.json()

#         # Process the search results and extract relevant information
#         if "items" in data:
#             results = data["items"]
#             if results:
#                 top_result = results[0]  # Get the top result
#                 title = top_result["title"]
#                 snippet = top_result["snippet"]
#                 link = top_result["link"]

#                 return f"Here is a top result from Google:\nTitle: {title}\nDescription: {snippet}\nLink: {link}"

#     except requests.RequestException:
#         return "An error occurred while searching on Google. Please try again."

#     return "No relevant information found."


def search_on_google(query):
    if query.lower().startswith("google"):
        query = query[6:].strip()
    elif query.lower().startswith("search for"):
        query = query[10:].strip()

    # Set up the Google Custom Search API request
    api_key = "AIzaSyCOKkruMJU-wZLeTp9aGir375uFd-oywg8"
    cx = "b3fa7d955dd604a98"
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"

    try:
        # Send the API request and retrieve the search results
        response = requests.get(url)
        data = response.json()

        # Process the search results and extract relevant information
        if "items" in data:
            results = data["items"]
            if results:
                # Display up to 10 results
                result_count = min(len(results), 3)
                output = f"Here are the top {result_count} results from Google:\n"

                for i in range(result_count):
                    result = results[i]
                    title = result["title"]
                    snippet = result["snippet"]
                    link = result["link"]
                    output += f"\nResult {i+1}:\nTitle: {title}\nDescription: {snippet}\nLink: {link}\n"

                return output

    except requests.RequestException:
        return "An error occurred while searching on Google. Please try again."

    return "No relevant information found."


# print(search_on_google("disha patni"))
'''----------------------------------------------------------------------------------------------------------------------------------------'''

# scanning the available Wi-Fi networks
# os.system('cmd /c "netsh wlan show networks"')
# # providing the Wi-Fi name as input
# router_name = input(
#     'Input Name/SSID of the Wi-Fi network we would like to connect: ')
# # connecting to the provided Wi-Fi network
# os.system(f'''cmd /c "netsh wlan connect name = {router_name}"''')
# print("If the system is not connected yet, try reconnecting to an earlier connected SSID!")

# -------------------------------------------------------------------------------------------------------------------------------------------

# import subprocess
#
# def My-wish():
#     MyWifi = subprocess.run (['netsh', 'interface', 'set', 'interface', "wi-fi", "ENABLED"])
# My-wish()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This function always tries to hit 'http://google.com' page when it is called. If it is able to reach this page, then return 'True' else 'False'.With which we can check our internet connected or not.

# def check_internet_connection():
#     try:
#         urllib.request.urlopen('http://google.com')
#         return True
#     except:
#         return False
