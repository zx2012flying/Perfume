# Perfume

This is producted by refering to https://github.com/hhursev/recipe-scrapers
The information of rating has been added.

         pip install git+git://github.com/zx2012flying/Perfume.git

How to use?
         from recipe_scrapers import scrape_me

         scrape_me = scrape_me(
         'https://www.fragrantica.com/perfume/Mugler/Angel-704.html'
         )

         print(scrape_me.title(), '\n')
         print(scrape_me.total_time(), '\n')
         print(scrape_me.ingredients(), '\n')
         print(scrape_me.instructions(), '\n')
         print(scrape_me.total_review(), '\n')
         print(scrape_me.review_score()) 




