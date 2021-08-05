a# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
from facebook_scraper import get_posts
posts = []
for post in get_posts('Ocoyoacac-Opina-543705549464114l', pages=2):
    print(post)
    posts.append(post)
df = pd.DataFrame(posts)

print(df)

df.to_csv('post.csv',index=False)