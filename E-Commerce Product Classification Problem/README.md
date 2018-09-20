# E-Commerce data classification problem

Training data has the following fields and contains 300000 records

Id - unique id for the record
additionalAttributes - Product attribute related to a particular product. These are key, value pairs that can be found in tabular format as product information for most products in e-commerce websites.

An example of additionalAttributes 

    {"ASIN": " B000JJRY9M", "Amazon Bestsellers Rank": "  in DVD & Blu-ray (See Top 100 in DVD & Blu-ray)",   "Average Customer Review": " Be the first to review this item",   "Classification": "  Exempt",   "DVD Release Date": " 26 Feb. 2007",   "Format": " AC-3, Colour, Dolby, DVD-Video, PAL",   "Language": " English",   "Number of discs": " 1",   "Region": " Region 2 (This DVD may not be viewable outside Europe. Read more about DVD formats.)",   "Run Time": " 287 minutes",   "Studio": " Hip-O Records"}

  

3. label   - The class to which a product belongs. Values belong to the finite set (‘books’,’music’,
         ‘videos’,’rest’)

    The problem statement is to  classify the products into any one of the buckets 
(i)   Books
(ii)  Music
(iii)  Videos
(iv)  Rest    -  A default class for products which doesn’t belong to (i),(ii) or (iii)  category.