from unique_queue import UniqueQueue
import requests

def extract_urls(html: str) -> list[str]:
    """Crude function to extract a list of URL links from a webpage."""
    urls: list[str] = []
    if '<a href="' in html:
        for x in html.split('<a href="')[1:]:
            url = x.split('"')[0]
            if 'choosealicense.com' in url and url.startswith('https://'):
                urls.append(url)
    return urls

# Seed URL to start traversal
seed_url = "https://choosealicense.com/"

# Initialize a UniqueQueue instance
q = UniqueQueue([seed_url])

# For the example, say this is what we're trying to solve:
# the number of time a string "example" appears
number_of_times_EXAMPLE_appears = 0

# Perform URL traversal
while not q.empty():
    # Get the next URL from the queue
    url = q.pop()

    # Load the page
    html = requests.get(url).text

    # Update the end result goal
    number_of_times_EXAMPLE_appears += html.lower().count('example')

    # Add the new URLs to search
    q.extend(extract_urls(html))
    
    # Print stats
    print(f"Completed: {q.completed_count()}. Remaining: {q.remaining_count()}.")

print(f"The string 'example' appears {number_of_times_EXAMPLE_appears} times on 'choosealicense.com'.")
