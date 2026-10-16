# Hire an IT 'Expert' 
### Let's put the **I** back in IT.

*A satirical Django job board for **humans** trying to prove they are still useful in a world that keeps asking AI to do everything.*

Our goal is to show you that you don't need AI.
....except in very rare cases, when it's us that need it.
> Our goal is to show you that you don't need AI.
>
> *...except in ***very rare cases***, when it's us that need it.*

##The idea behind the project

**Hire an IT 'Expert'** is a tongue-in-cheek take on the AI hype surrounding software development, the pressure to stay relevant, and the **wonderfully** unpredictable world of IT sector.


The company claims it wants to bring back what matters most: **people**. It presents its human IT experts, their skills, hourly rates and customer reviews while the little details tell a slightly different story. The top contributor has *definitely never used AI* nor is *AI*, unavailable employees are busy fixing things AI broke, and the company's supposedly honest reviews come with a little extra commentary of their own. The fun part comes when you try to delete an ***Employee***. 

The joke is not just in the copy. It is built into the application's behaviour: a missing candidate can leave **All-Mighty AI** as the top contributor, an employee marked unavailable gets a randomly selected excuse, and a new review gets a rating-dependent punchline added to it automatically. Also the About Us page tells everything you need to know. 

In other words: a recruitment website, a small workplace satire, and a very confident claim that this is all **100% human**. Allegedly.

##Where the satire lives
| Feature | What it does | The catch |
|---|---|---|
| **IT experts** | Browse professions, employee profiles, experience, skills, hourly rates and ratings. | The site insists its top contributor has *definitely never used AI*. |
| **The All-Mighty fallback** | Home page highlights the top-rated contributor when it exists. | With no rated candidates, the AI gets the spotlight instead(as usual). |
| **Availability status** | Employees can be marked as hired/unavailable. | Their status comes with an excuse, from fixing hallucinated imports to simply being lazy. |
| ** Honest reviews** | Leave, read, edit and delete employee reviews. | New reviews receive an extra randomly chosen punchline based on their rating. Transparency is important. |
| **Skills directory** | Browse skills, search by name and filter by selected skills. | At least the skills have unique names, so thats nice|
| ** Joining the team** | Create, edit, delete  an employee profile, if brave enough,  and follow the application flow. | The applicant is warned about being ghosted for months and is offered a very different career path, which they might like. |
| ** Customer support** | Visit the contact page and fill in the contact form. | The company praises its 24/7 live chat so enthusiastically that it sometimes sounds like the chat is an employee. |

## What you can do
- Browse a paginated directory of IT professionals and open individual profiles.
- Navigate to Home, About, Contact, Employees, Join Us, Reviews and Skills sections.
- Check review counts, average ratings and rating-based text in the interface.
- Create, read, edit and delete reviews for employees.
- Add new skills and associate them with employee profiles.
- Browse the skills directory, search for skills and filter the results.
- Mark an employee as hired/unavailable to see the current-task excuse displayed on the profile.
- Create, edit and delete employee profiles.
- View professions, experience, biography, hourly rate, skills, availability and review ratings.

## Built with
- **Python** and **Django**, application logic, models, forms and views.
- **Bootstrap 5** and custom CSS page layout and styling.
- **PostgreSQL** default local database.

## Project structure

|── core / # Home, About, Contact and a shared validation
|──employees/ # Employee profiles, skills, forms, views, managers, additional and custom tags
|── reviews/ # Reviews, ratings, forms, additional, views and custom 
|── templates/ # Base layout and page templates
|── static/ #CSS and other static assets
|── requirements.txt # Main dependencies
|── requirements-postgres.txt # Main dependencies plus PostgreSQL driver


## The main modules
- **`Employee`** ,  profile information, profession, experience, hourly rate, biography, photo, skills and availability. Delete and Edit form included for both employee and reviews.
- **`Skill`** , a uniquely named skill that can be newly added or  associated with multiple employees.
- **`Review`** , an author's review and rating for one employee, with a creation timestamp.


## Run it locally

### 1. Clone the repository
### 2. Create and activate a virtual environment
### 3. Install the dependencies
### 4. Create the database tables
### 5. Start the development server

## Quick tour for reviewers
1. Select **Join us** to create an employee profile and follow the application's response (It's better to start with skills if the employee has any).
2. Open **Employees** Browse the available profiles. Open a profile to see its information, skills, rating and current status.
3. Open **Skills** to add a skill, search by name or filter the list.
4. Use **Leave review** or an employee's review section to create a review, then browse, edit or delete reviews. Try and see the generated reviews as well. 
5. Mark an employee as hired and look for the excuse shown in the employee listing.
6. Visit **About us** for the company's noble mission and **Contact us** for its very reassuring customer-support promises.
7. Delete an employee to check responses and the flow.

### A friendly disclaimer

##This is a project created for the **SoftUni Django Basics Regular Exam**. The product copy is intentionally ironic and a satire; the application demonstrates Django models and relationships, forms and validation, function-based and class-based views, CRUD operations, template inheritance, custom template tags/filters and navigation.##




