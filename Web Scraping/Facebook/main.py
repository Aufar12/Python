# https://pypi.org/project/facebook-scraper/
from facebook_scraper import get_posts

for post in get_posts('feelzesty', pages=2, options={"comments": True, "reactors": False}): # Jumlah maksimal komen yang di scrap bisa diubah di file package nya. Saat ini 5000
    print(post)
    print('----------------------------------------------------')