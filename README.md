
# Quorum Coding Challenge

## Requirements
    It necessary to have python installed 

## Run the script to see the answer
```
cd quorum-challenge
python main.py
```

## Deliverables

You will be provided with a list of legislators, bills, votes, and vote results as specified above. You’ll
be asked to answerthe following questions:

1. For every legislatorin the dataset, how many bills did the legislator support (voted forthe
bill)? How many bills did the legislator oppose?
```sh
    ###legislators-support-oppose-count.csv###
    id,name,num_supported_bills,num_opposed_bills
    904789,Rep. Don Bacon (R-NE-2),1,1
    1603850,Rep. Jamaal Bowman (D-NY-16),1,1
    1852382,Rep. Cori Bush (D-MO-1),1,1
    904796,Rep. Brian Fitzpatrick (R-PA-1),1,1
    15318,Rep. Andrew Garbarino (R-NY-2),1,1
    1269775,Rep. Anthony Gonzalez (R-OH-16),1,1
    412649,Rep. John Katko (R-NY-24),1,1
    412421,Rep. Adam Kinzinger (R-IL-16),1,1
    15367,Rep. Nicole Malliotakis (R-NY-11),1,1
    412487,Rep. David McKinley (R-WV-1),1,1
    1269767,Rep. Alexandria Ocasio-Cortez (D-NY-14),1,1
    905216,Rep. Ilhan Omar (D-MN-5),1,1
    1269778,Rep. Ayanna Pressley (D-MA-7),1,1
    412393,Rep. Tom Reed (R-NY-23),1,1
    400380,Rep. Chris Smith (R-NJ-4),1,1
    1269790,Rep. Rashida Tlaib (D-MI-13),1,1
    400414,Rep. Fred Upton (R-MI-6),1,1
    17941,Rep. Jeff Van Drew (R-NJ-2),1,1
    400440,Rep. Don Young (R-AK-1),1,1
    412211,Rep. John Yarmuth (D-KY-3),0,0
```

2. For every bill in the dataset, how many legislators supported the bill? How many legislators
opposed the bill? Who was the primary sponsor of the bill?

```sh
    ###bills.csv###

    id,name,supporter_count,opposer_count,primary_sponsor
    2952375,H.R. 5376: Build Back Better Act,6,13,Rep. John Yarmuth (D-KY-3)
    2900994,H.R. 3684: Infrastructure Investment and Jobs Act,13,6,Unknown
```

1. Discuss your solution’s time complexity. What tradeoffs did you make?
```
    I chose the computational cost trade-off of reading line by line (stream data),
    over the computational cost of machine resources where it would store the entire
    file in memory to search for the legislator id, 
    (thinking on a massive scale of government data)
```

2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?
```
    The way it is implemented today, we would need to add more states in hard code,
    but we could take advantage of the header to get the index of the
    CSV value to make it dynamic with future data.
```
3. How would you change your solution if instead of receiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?
```
    We would refactor the file reading class to read the 
    provided list based on a multidimensional array.
```
4. How long did you spend working on the assignment?
```
    4 hours in total
    1 hour - Reviewing and updating documentation
    3 hours - Understanding the task and developing the code
```
