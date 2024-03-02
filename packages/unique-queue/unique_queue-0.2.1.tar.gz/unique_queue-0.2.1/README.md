# UniqueQueue

A Python UniqueQueue class - a FIFO queue, but which ignores attempts to re-add duplicate items, even after they're popped.

## Usage
```python
from unique_queue import UniqueQueue

# Initialize a UniqueQueue with optional initial items
my_queue = UniqueQueue(['a', 'b', 'c'])

# Push items into the queue
my_queue.push('d')

# Pop an item from the queue
popped_item = my_queue.pop()

# Extend the queue with multiple items
my_queue.extend(['e', 'f', 'g'])

# Get the total count of unique items in the queue
total_count = my_queue.total_count()

# Get the count of completed items (i.e., items that have been popped)
completed_count = my_queue.completed_count()

# Get the count of remaining items in the queue
remaining_count = my_queue.remaining_count()

# Check if the queue is empty
is_empty = my_queue.empty()

# Get the length of the queue
queue_length = len(my_queue)
```

## Methods

- `push(item)`: Adds an item to the queue if it is not already present.
  
- `pop()`: Removes and returns the first item from the queue.
  
- `extend(items: Iterable)`: Extends the queue with multiple items.
  
- `total_count()`: Returns the total count of unique items in the queue.
  
- `completed_count()`: Returns the count of completed items (i.e., items that have been popped).
  
- `remaining_count()`: Returns the count of remaining items in the queue.
  
- `empty()`: Returns `True` if the queue is empty, `False` otherwise.
  
- `__len__()`: Returns the length of the queue.

## Example

When doing activities like web scraping, you must keep a queue of pending pages to visit/scrape, based on links found on already-scraped pages. You must also avoid re-visiting already-visited pages, or risk duplicates in the output dataset.

This is an example of one such simple scraper:

```python
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
```
