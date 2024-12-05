
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# OCCT Bus App Redesign
## CS110 Final Project  Fall, 2024

## Team Members

Jake Steck, Ryan Tsui

***

## Project Description

Making a redesigned version of the OCCT bus app/website to make it more simplified, accurate, and easier to use.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1.  Main Menu with all bus routes and other functions 
2.  Bus schedules for each route 
3.  Map function to view bus stop location 
4.  ETA function to estimate how far away in mins a bus is from a given stop 
5.  Feedback Menu for improvements 

### Classes

- << You should have a list of each of your classes with a description >>

## ATP
Test Case 1: Main Menu
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Launch application   |Application opens to main menu     |
|  2                   | Observe main menu screen   | All bus route, map, status, and tips boxes are displayed |

Test Case 2: Bus Route Navigation
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click on each bus route box  |Each bus route box is clickable  |
|  2                   | Observe navigation to respective route list   | Correctly navigates user to correct bus route list for each respective route  |

Test Case 3: Map Functionality
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click map box  |Navigates user to Google Maps API |
|  2                   | Observe Google Maps API   | Bus routes mapped correctly on Google Maps API  |

Test Case 4: Status Functionality
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click status box  |Navigates user to status page |
|  2                   | Observe status page   | Status box displays updates/news |

Test Case 5: Tips Functionality
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click tips box  |Navigates user to tips page |
|  2                   | Observe tips page   | Tips page displays app usage guide |