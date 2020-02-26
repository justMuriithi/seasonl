# seasonl

Each season, clients purchase products on credit, and over the course of a season, they repay
their credit, and so clients have credit associated with them on a season-by-season basis. When a client makes a payment, we need to know which season the payment will be applied to,
as sometimes clients can have outstanding credit (debt) in more than one season. Since we still require that each saved repayment must
be associated with a season in our database, this offers greatuser experience in offering seasonless repayments where repayments are effected in a cascading fashion.

### How can this be manually tested?
 
 - Clone the repo 
- Install a virtual environment and activate 
- Run `pip install -r requirements.txt`
 - Run `python manage.py makemigrations`
 - Run `python manage.py migrate`
- Run the server `python manage.py runserver`
- use your browser to hit 
 `http://127.0.0.1:8000/`
 
 ### Test data (repayment Upload)
 - [x] seasonID provided
 ```source-json
 {
     "CustomerID": 4,
     "SeasonID": 110,
     "Amount": 7900.0,
     "Date": 12-11-2011
 }
 ```
  - [x] seasonID not provided
 ```source-json
 {
     "CustomerID": 9,
     "SeasonID": null,
     "Amount": 7900.0,
     "Date": 12-11-2011
 }
 ```
 
 ### Post-mortem
a. Current project status
  Ongoing with the following areas covered
  -[x] Cascade
  -[x] Overpaid
  -[x] Basic Interface
  -[x] Test data


b. Estimate on the outstanding work
Requiring 1 week to cover
  - Override
  - Repayment history signs


c. Successes/what went well
  - [x] Having MVP 

d. Bumps/what you wished went better
  - [x] Meeting all deliverables

- i. How you would improve your approach in future projects
- [x] Take greater advatage of the pair programming sessions to improve my problem solving efficiency

e. Improvements/enhancements to this project for future consideration 
  - [x] unit tests

 
 
