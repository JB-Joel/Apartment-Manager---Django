## Apartment Manager _(Django)_
_Work in Progress_.<br>
<b>Motivation:</b> Instead of keeping tenants' payment history on paper in a tabulated 1000-page ledger like my mom, what if you could keep track of payments with just a few clicks? What if you could type the name of a tenant, or search by apartment name instead of looking through different tables on different pages? What if you could view reports of payment history from 5 years ago with just a few clicks? Well, you'll be able to do all that and much more with this web app.
<br><br>A full web app to manage rental apartments, keep track of financial details, and provide visual reports of payment history. I used django for the backend and plan to use react to improve UI responsiveness and design. I'm currently using the python built-in SQLite database for storing/retrieving user information. I will later connect to a postgreSQL for scaling purposes. I also use Django's bulit-in authentication tools to implement user account creations, password resets and logins.
<br>After creating a user account, the landloard or apartment manager can perform the following tasks:
- Create and add apartments (specify apartment details like number of rooms, and features included)
-  set rent amount for different apartment types
-  view apartments' status _(occupied, available)_
-  Add tenants to apartments
-  Store records of previous and current apartment owners
-  View tenant standing and payment due dates
-  create visual reports of payment history
#### Prospective features
- A communication system (email/text) for managers to be able to send announcements/messages to all/individual tenants
- Notify tenants of bad standing? (tenants facing possible eviction?)
- 
