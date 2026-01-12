import requests
from ..models import FilmModel

SWAPI_API_URL = "https://swapi.dev/api/films/"


def fetchFilms():
    try:
        response = requests.get(SWAPI_API_URL,verify=False)
        response.raise_for_status()
        films = response.json()

        for film in films["results"]:
            swapi_id = int(film["url"].rstrip("/").split("/")[-1])

            FilmModel.objects.update_or_create(swapiFilm_id=swapi_id,
                defaults={
                    "film_title":film["title"],
                    "release_date":film["release_date"]
                })
    
    except requests.RequestException as e:
        print(f"Error fetching films: {e}")