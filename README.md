# streaming_anime_series
Goal: Python web scraping framework to scrape streaming data 

Functions of scraper:
* Get All Character wise Anime Data (Approx : 10000+)
* Get All Episode details of the particular Anime
* Get All Images Link of the Anime like anime thumb and banner images
* Get Episode Release Date
* Get Total Episodes in an Anime

Steps to be followed to scrape the data:
Suppose we want to gather data for all Animes starting from special characters then the scraper
should follow below steps
1. Visit Link https://animeseries.so/search/character=special
2. Get All Anime List Starting from special characters
3. Get List of All Episodes in all these animes
4. Get Related data
    4.1. Anime Title
    4.2. Description
    4.3. Status
    4.4. releaseYear
    4.5. Genre
    4.6. Slug (automatically generated)
    4.7. AnimeImage:
    4.8. TotalEpisodes
    4.9. EpisodeLinks
5. Once the above data is retrieved, the scraper should scrape each individual link
gathered in EpisodeLinks array (step 4.9)
6. Upon Visiting each episode link, the scraper should get the episode video iframe link
which can be found using below jquery selector
                $('.row > .right > a')
7. Steps 5 to 6 should be repeated for all episodes belonging to particular Anime which is
gathered in step 4.9
8. Repeat Step 1 to 7 for all below characters
'special', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z'

You can refer the below array for sample of data:
{
AnimeId: 1,
AnimeName: '.Hack//G.U. Returner',
Description: 'hack//G.U. Returner is a single-episode OVA offered to fans who completed all
three GU Games, featuring characters from the .hack//G.U. Games and .hack//Roots.',
Status: 'Completed',
releaseYear: '2007',
Genre: 'Adventure Drama Game Harem Martial Arts Seinen',
Slug: 'hackgu-returner',
AnimeImage: 'https://gogocdn.net/images/anime/5745.jpg',
TotalEpisodes: 1,
EpisodeLinks: [ 'https://animeseries.so/watch/hackgu-returner-episode-1.html' ],
EpisodeData:{
AnimeId: 1,
EpisodeNumber: 1,
EpisodeIframeArray: [
'//gogoplay1.com/streaming.php?id=NDA3OTI=&title=.Hack%2F%2FG.U.+Returner+episode+1
&typesub=SUB',
'//gogoplay1.com/embedplus?id=NDA3OTI=&token=E3QlStTSqLBP2p4MtkL4Qw&expires=164
1404943',
'https://sbplay2.com/e/env0jxmpf678',
'https://hydrax.net/watch?v=ZzJf3-Ua0',
'https://fembed-hd.com/v/8ylw3u8ld72r-4r',
'https://www.mp4upload.com/embed-e5t1flv0otkb.html',
'https://www.yourupload.com/embed/5U8C888IAc4w',
'https://dood.ws/e/pkjocerv9ic3'
]
}
