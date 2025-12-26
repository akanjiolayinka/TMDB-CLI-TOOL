"""TMDB API Client Module"""
import os
import requests
from typing import Dict, List, Optional


class TMDBClient:
    """Client for interacting with The Movie Database API"""
    
    BASE_URL = "https://api.themoviedb.org/3"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize TMDB Client
        
        Args:
            api_key: TMDB API key. If not provided, will try to read from TMDB_API_KEY env variable
        """
        self.api_key = api_key or os.getenv('TMDB_API_KEY')
        if not self.api_key:
            raise ValueError("TMDB API key is required. Set TMDB_API_KEY environment variable or pass it directly.")
        
        self.session = requests.Session()
        self.session.params = {'api_key': self.api_key}
    
    def _make_request(self, endpoint: str) -> Dict:
        """
        Make a request to TMDB API
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            JSON response as dictionary
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Please check your internet connection.")
        except requests.exceptions.ConnectionError:
            raise Exception("Failed to connect to TMDB API. Please check your internet connection.")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise Exception("Invalid API key. Please check your TMDB_API_KEY.")
            elif response.status_code == 404:
                raise Exception("Resource not found.")
            else:
                raise Exception(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred: {e}")
    
    def get_now_playing(self) -> List[Dict]:
        """Get list of movies currently playing in theaters"""
        data = self._make_request("/movie/now_playing")
        return data.get('results', [])
    
    def get_popular(self) -> List[Dict]:
        """Get list of popular movies"""
        data = self._make_request("/movie/popular")
        return data.get('results', [])
    
    def get_top_rated(self) -> List[Dict]:
        """Get list of top-rated movies"""
        data = self._make_request("/movie/top_rated")
        return data.get('results', [])
    
    def get_upcoming(self) -> List[Dict]:
        """Get list of upcoming movies"""
        data = self._make_request("/movie/upcoming")
        return data.get('results', [])
