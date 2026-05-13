Type Casting (.astype()): This is a low-level operation. It tells the computer, "Take this block of memory and treat it as this specific data type." In Java, this is equivalent to (int) myDouble. It is fast because it assumes the data is already in a compatible format and just needs a new label.

Parsing (pd.to_datetime()): This is a high-level, intelligent function. It looks at the content of the data (like the string "05/03/2016") and tries to figure out what is the year, month, and day.
--------------

Ok so i ran .as_type and it worked but if there was one missing value my program would have crashed so if i set .as_type(errors=raise ) it will rasie it but if i do 
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
it will never crash 
and it will make a special version of Nan called Nat 
and i can see how many Nats are there by doing .isna().sum()

----------------------

What is dt in pandas?
When you convert a column to datetime format — which you already did with pd.to_datetime() — pandas stores that column as a special type called datetime64. Now that column isn't just text anymore. It actually understands that 2016-05-03 17:30:00 has a year, a month, a day, an hour, a minute, and a second as separate components.
But here's the thing — you can't just type df["Date"].hour and expect it to work. Pandas needs you to go through a gateway first. That gateway is .dt
Think of .dt like a toolbox. The column is the toolbox, and .dt opens it. Once it's open, you can pull out any individual component you want.

Everything inside the .dt toolbox
These are all the things you can extract from a datetime column using .dt:

.dt.year — gives you the year → 2016
.dt.month — gives you the month as a number → 5 (for May)
.dt.day — gives you the day of the month → 3
.dt.hour — gives you the hour in 24hr format → 17
.dt.minute — gives you the minute → 30
.dt.second — gives you the second → 0
.dt.date — gives you just the date part, no time → 2016-05-03
.dt.time — gives you just the time part, no date → 17:30:00
.dt.dayofweek — gives you the day of the week as a number → 0 is Monday, 6 is Sunday
.dt.day_name() — gives you the day as text → "Tuesday"
.dt.month_name() — gives you the month as text → "May"
.dt.quarter — gives you which quarter of the year → 1, 2, 3, or 4
.dt.week — gives you which week number of the year → 1 through 52
.dt.is_month_start — gives you True or False, is this the first day of the month
.dt.is_month_end — same idea, last day of the month
.dt.is_weekend — doesn't exist natively, but you can derive it from .dt.dayofweek being 5 or 6

------------
The code to print the YES OR NO is SWARMPLOT not scatterplot as it will clearly depcit YES OR NO but actually scatterplot will plot FOR  EACH point it will literally eay all the moemery so better than that was bar plot which i didnt know. 

--------------

I used bar graph is is discrete I need a better understanding of when to use what graph.


-------
when u commit u can use two -m -m the first -m means the git name and the second is descrption.

git commit --amend --no-edit

