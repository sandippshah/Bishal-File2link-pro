from biisal.vars import Var
from biisal.bot import StreamBot
from biisal.utils.human_readable import humanbytes
from biisal.utils.file_properties import get_file_ids
from biisal.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp
import jinja2
import re
from imdb import IMDb


async def fetch_imdb_data(movie_name):
    ia = IMDb()
    movies = ia.search_movie(movie_name)
    if not movies:
        return None
    movie = movies[0]
    ia.update(movie)
    return {
        "title": movie.get('title'),
        "year": movie.get('year'),
        "rating": movie.get('rating'),
        "plot": movie.get('plot outline'),
        "cover_url": movie.get('cover url')
    }


def clean_file_name(file_name):
    # Define blacklist words
    blacklist_words = ["mkv", "x264", "x265", "mp4"]  # Add actual blacklist words here

    # Remove Telegram usernames (assuming they start with '@')
    file_name = re.sub(r'@\w+', '', file_name, flags=re.IGNORECASE)

    # Remove special characters
    file_name = re.sub(r'[_\.\[\]\':"+]', ' ', file_name)

    # Remove blacklist words
    for word in blacklist_words:
        file_name = re.sub(word, '', file_name, flags=re.IGNORECASE)

    # Remove extra spaces
    file_name = ' '.join(file_name.split())

    return file_name

async def render_page(id, secure_hash, src=None):
    file = await StreamBot.get_messages(int(Var.BIN_CHANNEL), int(id))
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f"link hash: {secure_hash} - {file_data.unique_id[:6]}")
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash

    src = urllib.parse.urljoin(
        Var.URL,
        f"{id}/{urllib.parse.quote_plus(file_data.file_name)}?hash={secure_hash}",
    )

    tag = file_data.mime_type.split("/")[0].strip()
    file_size = humanbytes(file_data.file_size)
    if tag in ["video", "audio"]:
        template_file = "biisal/template/req.html"
    else:
        template_file = "biisal/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get("Content-Length")))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    file_name = clean_file_name(file_data.file_name)
    
    imdb_data = await fetch_imdb_data(file_name)
    
    
    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        file_unique_id=file_data.unique_id,
        imdb_data=imdb_data
    )    
    

