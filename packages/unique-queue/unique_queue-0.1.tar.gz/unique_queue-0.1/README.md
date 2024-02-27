# UniqueQueue

A Python UniqueQueue class - a FIFO queue, but which ignores attempts to re-add duplicate items, even after they're popped.

## Example

When doing activities like web scraping, you must keep a queue of pending pages to visit/scrape, based on links found on already-scraped pages. You must also avoid re-visiting already-visited pages, or risk duplicates in the output dataset.

```python
from unique_queue import UniqueQueue

uq = UniqueQueue()
```
