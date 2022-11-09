  **Deploy on your Local Server :** 
   * update pip 
   >python -m pip install --update pip
   * install git in your desktop
   * create new folder and run
   >git init
   * now clone the repository
   >git clone https://github.com/Divyansh6799/Foodie-s-World-Web-Applications-Django-
   * open food-recipe-web-app
   >cd food-recipe-web-app
   * to start virtual environment 
   >...\food-food-recipe-web-app>myvenv\Scripts\activate
   * now run 
   >pip install -r requirements.text
   * now run 
   >python manage.py runserver
   * run http://127.0.0.1:8000/ on your browser 
  
  **Details about the web-app** :<br> 
    this web app has been made using Django Framework. Sqlite3 Relational DBMS has been used which is a default DBMS for django.
    To query the database django Queryset has been used. "fooddetail" model has been created which contains "author" as a ForeignKey  attribute which is primary key for inbuilt user model. "fooddetail" model contains fields : name ,description ,ingredients,steps,image .
    you have to install pillow which supports in accessing images
    >pip install pillow 
    Html, css and bootstrap has been used to design the frontend.
    I have made this site online by uploading it on pythonanywhere web hosting server.


Demo Pics----
![demo](https://github.com/Divyansh6799/Foodie-s-World-Web-Applications-Django-/blob/master/Screenshot%20(11).png)
![demo](https://github.com/Divyansh6799/Foodie-s-World-Web-Applications-Django-/blob/master/Demo/Screenshot%20(12).png)
![demo](https://github.com/Divyansh6799/Foodie-s-World-Web-Applications-Django-/blob/master/Demo/Screenshot%20(14).png)

