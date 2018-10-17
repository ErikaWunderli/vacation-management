Vacation Management application

In its present state, the front-end and the backend are not connected, it is still missing JSON and AJAX.
So far, I have created a login and a logout page, and different interfaces for Viewers, Employees and Admins.
Some features on the front-end work: navlinks can be used for navigating on the page, you can log out, and if you 
wish to send an email, you are directed to the email client.
If you hit delete, the record will disappear from the DOM and from the database as well. However, the other requests
are yet to be coded. 


Once the application is finished, after the setup of the backend, it will load the Login page. 
After checking the user's status in the database, it will load the page that matches the user's role.
Then, they will be able to access the calendar view only if their status is "Viewer". Employees can view, 
create or delete their leave requests. Admins will have access to all the users' status, they can modify them, overview 
all pending requests and change them, and send a notification via email if they want. Plus, they can also send their
leave requests, delete or view them as well. 
