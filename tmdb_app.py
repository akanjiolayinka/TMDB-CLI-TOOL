#!/usr/bin/env python3
"""TMDB CLI Application - Main Entry Point"""
import argparse
import sys
from typing import List, Dict
from tmdb_client import TMDBClient


def format_movie_output(movies: List[Dict]) -> None:
    """
    Format and print movie information to terminal
    
    Args:
        movies: List of movie dictionaries from TMDB API
    """
    if not movies:
        print("No movies found.")
        return
    
    print(f"\n{'='*80}")
    print(f"Found {len(movies)} movies:")
    print(f"{'='*80}\n")
    
    for idx, movie in enumerate(movies, 1):
        title = movie.get('title', 'N/A')
        release_date = movie.get('release_date', 'N/A')
        rating = movie.get('vote_average', 'N/A')
        overview = movie.get('overview', 'No overview available.')
        
        # Truncate overview if too long
        if len(overview) > 150:
            overview = overview[:147] + "..."
        
        print(f"{idx}. {title}")
        print(f"   Release Date: {release_date}")
        print(f"   Rating: {rating}/10")
        print(f"   Overview: {overview}")
        print(f"{'-'*80}")


def main():
    """Main CLI application logic"""
    parser = argparse.ArgumentParser(
        description='TMDB CLI Tool - Fetch and display movie information from The Movie Database',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  tmdb-app --type playing     # Show now playing movies
  tmdb-app --type popular     # Show popular movies
  tmdb-app --type top         # Show top-rated movies
  tmdb-app --type upcoming    # Show upcoming movies
        """
    )
    
    parser.add_argument(
        '--type',
        type=str,
        required=True,
        choices=['playing', 'popular', 'top', 'upcoming'],
        help='Type of movies to fetch (playing, popular, top, upcoming)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize TMDB client
        client = TMDBClient()
        
        # Fetch movies based on type
        print(f"Fetching {args.type} movies from TMDB...")
        
        if args.type == 'playing':
            movies = client.get_now_playing()
            print("Now Playing Movies")
        elif args.type == 'popular':
            movies = client.get_popular()
            print("Popular Movies")
        elif args.type == 'top':
            movies = client.get_top_rated()
            print("Top Rated Movies")
        elif args.type == 'upcoming':
            movies = client.get_upcoming()
            print("Upcoming Movies")
        
        # Display results
        format_movie_output(movies)
        
    except ValueError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        print("\nPlease set your TMDB API key:", file=sys.stderr)
        print("  export TMDB_API_KEY='your_api_key_here'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
