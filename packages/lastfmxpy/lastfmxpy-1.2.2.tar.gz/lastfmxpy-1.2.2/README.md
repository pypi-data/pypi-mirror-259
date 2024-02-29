# Last FM API (lastfmxpy)

![GitHub License](https://img.shields.io/github/license/pkeorley/telegram-tui)
![GitHub issues](https://img.shields.io/github/issues/pkeorley/telegram-tui)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/pkeorley/lastfmxpy)
![GitHub contributors](https://img.shields.io/github/contributors/pkeorley/lastfmxpy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lastfmxpy.svg)](https://pypi.org/project/lastfmxpy)
[![PyPI - Version](https://img.shields.io/pypi/v/lastfmxpy.svg)](https://pypi.org/project/lastfmxpy)

-----

* **lastfmxpy** *(Last FM Api)* - is a mono-repository that has a user-friendly interface for interacting with the largest music service [last.fm](https://www.last.fm). This library implements all the standard methods available on [this page](https://www.last.fm/api).

**Table of contents**
- [Project goals](#project-goals)
- [Documentation](#documentation)
- - [Installation](#installation)
- - [Synchronous usage](#example-of-synchronous-usage)
- - [Asynchronous usage](#example-of-asynchronous-usage)
- - [All available methods](#all-available-methods)
- - [All available parameters](#all-available-parameters)
- [Licence](#license)

## Project goals
- [x] Implement all existing methods in the [Last FM API Docs](https://www.last.fm/api)
- [x] Provide a convenient interface for sending requests to the server
- [x] Add doc-strings to each method or class
- [x] Add asynchronous support
- [ ] Add tests
- [ ] Add support for documentation in different languages

## Documentation
This documentation provides examples of how to use the **synchronous** and **asynchronous** classes and methods,
and shows all available **methods** and **parameters**

### Installation
To install this library, you need to enter the following command
```shell
pip install -U lastfmxpy
```

### Example of SYNCHRONOUS usage
In this example, we use the `LastFMApi` class that we previously imported from the `api` package,
and then use the post method in which we set the method we will use and the parameter
```python
import json

from lastfmxpy import (
    api,
    methods,
    params,
)

# Initialise our object through which we will interact with last.fm
client = api.LastFMApi(
    api_key="...", # Get here https://www.last.fm/api/account/create,
    shared_secret="..." # Also get here （￣︶￣）↗　
)

# Get all information about the artist in JSON as a string 
response: str = client.post(
    
    # Specify which method we will use
    method=methods.User.GET_INFO,
    
    # Let us specify our parameters
    params=params.UserGetInfo(
        user="pkeorley"
    ),
    
    # We can also specify additional parameters
    additional_params=dict(format="json")

)

# Let's show our data in a convenient form on the screen
data: str = json.dumps(
    json.loads(response),
    indent=4,
    ensure_ascii=False
)

print(data)
```

### Example of ASYNCHRONOUS usage
In this example, we use the `AsyncLastFMApi` class, which we previously imported from the `api`
package in the same way as in the case of the previous class, and then use 
the post method in which we set the method we will use and the parameter
```python
import asyncio
import json

from lastfmxpy import (
    api,
    methods,
    params,
)

# Initialise our object through which we will interact with last.fm
client = api.AsyncLastFMApi(
    api_key="...", # Get here https://www.last.fm/api/account/create,
    shared_secret="..." # Also get here （￣︶￣）↗　
)

# Get all information about the artist in JSON as a string 
async def main():
    
    # Calling the asynchronous method
    response: str = await client.post(
        
        # Specify which method we will use
        method=methods.User.GET_INFO,
        
        # Let us specify our parameters
        params=params.UserGetInfo(
            user="pkeorley"
        ),
        
        # We can also specify additional parameters
        additional_params=dict(format="json")
    
    )
    
    # Let's show our data in a convenient form on the screen
    data: str = json.dumps(
        json.loads(response),
        indent=4,
        ensure_ascii=False
    )

    return data

print(asyncio.run(main()))
```

#### All available methods:
```python
from lastfmxpy.methods import (
    Album,
    Artist,
    Auth,
    Chart,
    Geo,
    Library,
    Tag,
    Track,
    User
)
```

#### All available parameters:

```python
from lastfmxpy.params import (
    AlbumAddTags,
    AlbumGetInfo,
    AlbumGetTags,
    AlbumGetTopTags,
    AlbumRemoveTag,
    AlbumSearch
)

from lastfmxpy.params import (
    AlbumAddTags,
    AlbumGetInfo,
    AlbumGetTags,
    AlbumGetTopTags,
    AlbumRemoveTag,
    AlbumSearch
)
from lastfmxpy.params import (
    ArtistAddTags,
    ArtistGetCorrection,
    ArtistGetInfo,
    ArtistGetSimilar,
    ArtistGetTags,
    ArtistGetTopAlbums,
    ArtistGetTopTags,
    ArtistGetTopTracks,
    ArtistRemoveTag,
    ArtistSearch
)
from lastfmxpy.params import (
    AuthGetMobileSession,  # deprecated as last.fm
    AuthGetSession,
    AuthGetToken
)
from lastfmxpy.params import (
    ChartGetTopArtists,
    ChartGetTopTags,
    ChartGetTopTracks
)
from lastfmxpy.params import (
    GeoGetTopArtists,
    GeoGetTopTracks
)
from lastfmxpy.params import (
    LibraryGetArtists
)
from lastfmxpy.params import (
    TagGetInfo,
    TagGetSimilar,
    TagGetTopAlbums,
    TagGetTopArtists,
    TagGetTopTracks,
    TagGetWeeklyChartList
)
from lastfmxpy.params import (
    TrackAddTags,
    TrackGetCorrection,
    TrackGetInfo,
    TrackGetSimilar,
    TrackGetTags,
    TrackGetTopTags,
    TrackLove,
    TrackRemoveTag,
    TrackScrobble,
    TrackSearch,
    TrackUnlove,
    TrackUpdateNowPlaying
)
from lastfmxpy.params import (
    UserGetFriends,
    UserGetInfo,
    UserGetLovedTracks,
    UserGetPersonalTags,
    UserGetRecentTracks,
    UserGetTopAlbums,
    UserGetTopArtists,
    UserGetTopTags,
    UserGetTopTracks,
    UserGetWeeklyAlbumChart,
    UserGetWeeklyArtistChart,
    UserGetWeeklyChartList,
    UserGetWeeklyTrackChart
)
```

## License

`lastfmxpy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.