#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

base_url = "https://animeseries.so"
res = requests.get("https://animeseries.so/search/character=special")

soup = BeautifulSoup(res.content,'html.parser')


b = soup.find('ul',{'class' : 'items'})

lis = b.find_all('li')

def extract_href_anime_details(href):
       scrape_href_url = requests.get(base_url+href)
       href_soup = BeautifulSoup(scrape_href_url.content,'html.parser')
       href_scraped_elements = href_soup.find('div',{'class':"main_body"})
       inter_tags = href_scraped_elements.find('div', {'class' : "right"})

       #Description
       description = inter_tags.find('p').contents[0]
       #status
       status = inter_tags.find_all('a')
       a_tags = []

       for items in status:
              final_status = items.contents[0]
#       print(final_status)
              a_tags.append(final_status)
       anime_status = a_tags[2]
       anime_release_year = a_tags[3]

       a_genres =",".join(a_tags[4:])
       return description,anime_status,anime_release_year,a_genres,href_scraped_elements


def extract_episode_links(href_scraped_elements):
       #episode_links
       episodes = href_scraped_elements.find('div', {'class' : "list_episode"})
       final_episodes = episodes.findAll('a')
       total_episodes = len(final_episodes)
       episode_links = []
       episode_iframe_links = []
       episode_number_links = []
       for new_episodes in final_episodes:
              episode_href = new_episodes.get('href')
              episode_links_make = base_url+episode_href
              episode_links.append(episode_links_make)

       return total_episodes,episode_links
def arrange_iframes(episode_links):
       print("iframe looks like",episode_links)
       episode_iframe_links = []
       episode_number = 0
       #extract episode information
       episodes_scrape_url = requests.get(episode_links)
       episodes_scrape_url_content = BeautifulSoup(episodes_scrape_url.content,'html.parser')
       if len(episodes_scrape_url_content) > 0:
              list_episode_video = episodes_scrape_url_content.find('div', {'class' : "list_episode_video"})
              data_video = list_episode_video.find_all('a')
              for each_video in data_video:
                     episode_number = episode_number + 1
                     data_videos = each_video.get("data-video")
                     episode_iframe_links.append(data_videos)

       return episode_number,episode_iframe_links

anime_id = 0
anime_dict = {'AnimeId':'','AnimeName':'','Description':'','Status':'','releaseYear':'','Genre':'','Slug':'',
              'AnimeImage':'','TotalEpisodes':'','EpisodeLinks':'',
              'EpisodeData': {'AnimeId':'','EpisodeNumber':'','EpisodeIframeArray':''}}

for links in lis:
       #extract base level information
       anime_id = anime_id + 1
       anime_link = links.find('a')
       href = anime_link.get('href')
       if (href == "/anime/hackgu-returner.html" or href == "/anime/hackliminality-dub.html"):
              title = anime_link.get('title')
              anime_url = links.find('div', {'class' : "thumb_anime"})
              url = anime_url.get('style')
              ptr = re.search("https.*[)]",url) # regex to search url till ')'
              final_url = url[ptr.start():ptr.end()-2] # end() -1 to remove ')'

              description,anime_status,anime_release_year,a_genres,href_scraped_elements = extract_href_anime_details(href)
              total_episodes,all_episode_links = extract_episode_links(href_scraped_elements)
              anime_dict['AnimeId'] = anime_id
              anime_dict['AnimeName'] = title
              anime_dict['Description'] = description
              anime_dict['Status'] = anime_status
              anime_dict['releaseYear'] = anime_release_year
              anime_dict['Genre'] = a_genres
              anime_dict['AnimeImage'] = final_url
              anime_dict['TotalEpisodes'] = total_episodes
              anime_dict['EpisodeLinks'] = all_episode_links

              for episode_links in all_episode_links:
                     episode_data_list = []
                     episode_number,episode_iframe_links = arrange_iframes(episode_links)
                     anime_dict['EpisodeData']['AnimeId'] = anime_id
                     anime_dict['EpisodeData']['EpisodeNumber'] = episode_number
                     anime_dict['EpisodeData']['EpisodeIframeArray'] = episode_iframe_links
                     episode_data_list.append(anime_dict['EpisodeData'])

                     print(episode_data_list)
                     anime_dict['EpisodeData'] = episode_data_list
              print(anime_dict)


