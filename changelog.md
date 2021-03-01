# RPG: Oregon Trail Changelog
[v0.1] - 2021-01-14
- File created
- Basic numerical inventory created

[v0.2] - 2021-02-04
- Introductory menus added
- Player attributes defined
- Placeholder numerical inventory removed

[v0.3] - 2021-02-05
- Store interface created
- Added name selection for player
- Added party members + name selection for them
- Added story elements
- Added date of departure selector

[v0.4] - 2021-02-18
- Created map
- Removed redundant files

[v0.5] - 2021-02-20
- Added exceptions for value errors

[v0.6] - 2021-02-21
- Added trail
- Added random events

[v0.7] 2021-02-22
- Fixed issue with date storing
- Added functions to set weather type
- Added Weather globals
- Removed redundacies
- Added new options to trail.py

[v0.8] 2021-02-23
- Fixed error where main.py was replaced with map.py
- Missing comments and docstrings added
- Fixed comment mistypes on 2 comments
- Fixed error where illnesses cant trigger death
- Fixed error when getting shot 
- Improved main menu by adding keyboard selection
- Fixed bug where only banker could be selected for a job

[v0.9] 2021-02-24
- Added locations
- Added loops
- Fixed formatting issues

[v1.0] 2021-02-28
- Changed nested ifs to "and" strings
- Fixed bug where player cant return to main menu after opening changelog
- Added exceptions for ValueErrors
- Fixed unreasonable penalties when missing shots while hunting
- Fixed unbroken loop in cold_weather event
- Added distance to next landmark counter
- Changed events colour library from rich to colorama to better format the fort
  store UI
- Added the abulity to finish the game after reaching mile goal
- Fixed error where dates was no longer imported into gameglobals
- Added branching paths to south pass and blue mountains landmarks
- Fixed bug where the distance to the next landmark could become a negative
  integer
- Changeed nested ifs to "and" strings to make code less terrible
- Player can now win battles with wild animals
- Added option to talk to strangers, messages change based on location
- Fixed bug where getting a disease crashes the game
- Fixed a bug where if a party member dies from a disease the next member to
  become afflicted would cause an error when checking member list length
- Fixed a bug where when choosing a path and selecting the map will cause the
  player to be unable to choose a path
- Made food decrease as player walks the trail, amount decreses depending on
  food ration setting
- Fixed bug where next landmark goes into the negatives
- Fixed bug where choosing to look at the map at a crossroads makes it so you 
  can't choose where to go
- Fixed bug where player can die of a snake bite because there's no medicine
  but was never given the option to buy medicine
- Fixed bug when in the fort store the keyboard inputs only sometimes do what's
  listed on screen
- Fixed bug where player randomly lose thousands of bullets
- Fixed bug where weather is always fine and player health is always healthy
- Fixed bug where prices in the fort store don't match what's deducted from 
  your balance
- Fixed bug where money randomly resets back to 1600
- Made something happen when selecting map option
- Fixed bug where distance to landmark can be negative
- Fixed bug where player can't return to main menu after opening changelog
- Added more exceptions for ValueErrors
