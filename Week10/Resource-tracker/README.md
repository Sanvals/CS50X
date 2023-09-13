# Resource Tracker
#### Video Demo:  https://youtu.be/F8a0Vs0adwU
#### Description: A resource tracker for your favorite role-playing games

## Technologies used
This program uses a combination of **HTML**, **JavaScript**, **CSS** and **Python**. The front-end is a series of HTML pages interconnected in **FLASK**, embellished with the lastest version of **Bootstrap**.

## How does it work
The user is first prompted into a log-in page. For the purposes of the present project, all the users have access to the same main page. The main page is supposed to display all the resources the role-playing party possesses at a given time, and any of the players who is logged-in should be able to see and update the page.

Once on the main page, there are a few sections: coins, food and items.

>⚠️ For checking purposes, it's easier just to go with admin/admin.

## Coins
On the coins section, players can update their wealth by *spending* or *earning* coins. The way the database is updated is via *submit* button on the dedicated portion of the page. Once the user clicks on *submit*, **Python** checks if the input is valid and within range, refreshing the page if something goes wrong.

As a side note, all the transactions are saved individually, being possible to trace back any wrong or mistaken input the users may have sent. **Python** shows only the last modified entry of the *coins* table.

>💡 Ideas for future improvements: output a second chart for the currency owned ony by the logges-in person.

## Food
On the food section we can keep track of the rations. It's possible to add and delete items, but it's also possible to add or subtract elements individually if necessary.

>💡 Ideas for future improvements: display a slider on the page and make it "consume" days from the rations.

## Items
This displays a little list of the owned items. It's possible to unfold each item and see their description and modify it if necessary. **Python** extracts the full list of items and then the **HTML** page parses the object and displays the amount of items per category.

>💡 Ideas for future improvements: Make the header categories also fold or unfold items.

# Project structure
The main folder contains the following files
- app.y, with the body of the **FLASK** program,
- helpers.py, with some functionality for **FLASH** to run,
- track.db, the database for the project.

Inside, we have the folder *templates* with three documents
- index.html, with the main page of the project,
- login.html, for the check-in access,
- layout.html, which serves as the **FLASK** template.

It's also included a folder called *static* that contains
- styles.cc, helping the project to override **Bootstrap** styles.

Thank you for reading this!