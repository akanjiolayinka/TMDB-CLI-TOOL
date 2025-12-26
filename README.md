# TMDB CLI Tool

A command-line interface (CLI) application to fetch and display movie information from [The Movie Database (TMDB)](https://www.themoviedb.org/) API.

## Features

- Fetch and display **Now Playing** movies
- Fetch and display **Popular** movies
- Fetch and display **Top Rated** movies
- Fetch and display **Upcoming** movies
- Clean and formatted terminal output
- Graceful error handling for API failures and network issues

## Prerequisites

- Python 3.7 or higher
- TMDB API Key (free - get it from [TMDB API Settings](https://www.themoviedb.org/settings/api))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akanjiolayinka/TMDB-CLI-TOOL.git
   cd TMDB-CLI-TOOL
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your TMDB API key:**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your TMDB API key:
   ```
   TMDB_API_KEY=your_actual_api_key_here
   ```
   
   Alternatively, export it as an environment variable:
   ```bash
   export TMDB_API_KEY='your_actual_api_key_here'
   ```

## Usage

Run the CLI tool with the `--type` argument to specify which type of movies you want to fetch:

```bash
python tmdb_app.py --type playing    # Now playing movies
python tmdb_app.py --type popular    # Popular movies
python tmdb_app.py --type top        # Top-rated movies
python tmdb_app.py --type upcoming   # Upcoming movies
```

### Make it executable (Optional)

For easier usage, you can make the script executable and create an alias:

```bash
chmod +x tmdb_app.py
```

Then create an alias in your `~/.bashrc` or `~/.zshrc`:
```bash
alias tmdb-app="python3 /path/to/TMDB-CLI-TOOL/tmdb_app.py"
```

After reloading your shell, you can use:
```bash
tmdb-app --type playing
tmdb-app --type popular
tmdb-app --type top
tmdb-app --type upcoming
```

## Example Output

```
Fetching popular movies from TMDB...
Popular Movies

================================================================================
Found 20 movies:
================================================================================

1. The Shawshank Redemption
   Release Date: 1994-09-23
   Rating: 8.7/10
   Overview: Framed in the 1940s for the double murder of his wife and her lover...
--------------------------------------------------------------------------------
2. The Godfather
   Release Date: 1972-03-14
   Rating: 8.7/10
   Overview: Spanning the years 1945 to 1955, a chronicle of the fictional...
--------------------------------------------------------------------------------
...
```

## Project Structure

```
TMDB-CLI-TOOL/
├── tmdb_app.py          # Main CLI application
├── tmdb_client.py       # TMDB API client module
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## API Endpoints Used

- **Now Playing**: `/movie/now_playing`
- **Popular**: `/movie/popular`
- **Top Rated**: `/movie/top_rated`
- **Upcoming**: `/movie/upcoming`

## Error Handling

The application handles various error scenarios:

- **Missing API Key**: Clear message with instructions to set the key
- **Network Issues**: Catches connection errors and timeouts
- **Invalid API Key**: Detects 401 authentication errors
- **API Failures**: Gracefully handles HTTP errors and displays user-friendly messages

## Getting Your TMDB API Key

1. Create a free account at [TMDB](https://www.themoviedb.org/signup)
2. Go to [API Settings](https://www.themoviedb.org/settings/api)
3. Request an API key (choose "Developer" option)
4. Copy your API key and use it in the application

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available for educational purposes.

## Acknowledgments

- Data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- This project uses the TMDB API but is not endorsed or certified by TMDB