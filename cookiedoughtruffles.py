ingredients = {'2.5 cups': 'all purpose flour','1 teaspoon':'salt','1 cup': 'butter','3/4 cups': 'sugar','3/4 cups': 'packed brown sugar','1 teaspoon': 'vanilla', '1/3 cup': 'milk','1 cup': 'mini semi-sweet chocolate chips', '14 oz': 'dark chocolate candy coating'}
directions =  ['1. Beat butter and sugars and in large bowl with electric mixer on medium speed until light and fluffy. Add cream and vanilla. Stir in flour and salt and mix on low speed (or by hand) until incorporated. Stir in chocolate chips.','2. Cover and chill dough for 1 hour.', '3. When dough is firm enough to handle (it may help to lightly flour your hands), form dough into 1″ balls and arrange on a baking sheet lined with waxed paper. Place sheets in freezer and let chill for 30 minute', '4. Melt chocolate candy coating in a double boiler or in microwave according to package directions. Using forks or a dipping tool, dip cookie balls into candy coating to cover. Tap fork on side of pan to remove any excess coating, and return to waxed paper-lined baking sheets. Chill until set.']

for ingredient, value in ingredients.items():
    print(value, ingredient);

for step in directions:
    print(step)
    print()
