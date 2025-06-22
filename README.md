# 🔍 Approach Explanation

### Target URL & Tools
- I targeted the GitHub Trending page: [https://github.com/trending](https://github.com/trending).
- I used Python with the `requests` library to fetch the webpage content, and `BeautifulSoup` for parsing and HTML extraction.

### Sending Request
- A GET request was sent to the GitHub trending page using a custom `User-Agent` to avoid being blocked by GitHub.

### Parsing HTML
- The HTML response was parsed using `BeautifulSoup`.
- I looked for `article` elements with the class `Box-row`, which represent individual trending repositories.

### Extracting Repository Data
- For each of the first 5 repositories, I extracted:
  - The repository's full path (e.g., `/owner/repo-name`) from the `<a>` tag inside the `<h2>`.
  - Constructed the full GitHub URL (e.g., `https://github.com/owner/repo-name`).
  - Formatted the data as `Repository Name` and `Link`.

### Saving to CSV
- The extracted data was saved to a CSV file named `trending_repos.csv` using Python’s `csv` module.
- The file contains two columns: **Repository Name** and **Link**.
