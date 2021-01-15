## Available Endpoints
tags
Route   /cocktails/tags/all
        Returns a list of cocktail tags

ingredients
route /ingredients/all

cocktails
cocktail detail http://127.0.0.1:8000/cocktails/<cocktail_name>
all         http://127.0.0.1:8000/cocktails/all
all by page http://127.0.0.1:8000/cocktails/all/<pagenumber>
all by page + quantity  http://127.0.0.1:8000/cocktails/all/<pagenumber>/<quantity>
all by page + quantity + tags http://127.0.0.1:8000/cocktails/all/<pagenumber>/<quantity>/<tags>


search
by list of ingredients http://127.0.0.1:8000/cocktails/filter/<ingredients>
by querystring         http://127.0.0.1:8000/cocktails/filter/search/<query>'

## to do
change all cocktail route to properly respond with all cocktails
change cocktail endpoint ordering to allow users to get all cocktails with specific tags
move tags out of cocktails into its own endpoint (/tags/all instead of /cocktails/tags/all)
change similar cocktails on cocktail detail page to be done by ingredients and tags
document endpoints
build frontend to explain documentations with sandbox for users to understand whats going on
secure certain routes (everything in bar)
implement api keys
