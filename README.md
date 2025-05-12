# Backend_Task 


**1) Installation Steps :**
   
      -> Download this folder
      
      -> Go to the main directory (faq_project)
      
      -> write this to activate the virtual environment in windows write "venv\Scripts\activate" or in linux write "source venv/bin/activate"
      
      -> Run python manage.py runserver to run a server.

**2) API Usage:**
   
   **Admin Panel**
   
   --> http://localhost:8000/admin/
   ![image](https://github.com/user-attachments/assets/9947f9bc-9d65-484a-8053-a62a00883726)

  --> http://localhost:8000/admin/faq_app/faq/
   ![image](https://github.com/user-attachments/assets/b4d83a6d-0aab-4867-bd38-5b731d7ff693)
   
  -->  Q and A with CKeditor
   ![image](https://github.com/user-attachments/assets/efa3c23a-bf16-4434-bb73-f22c63ed27cf)
   
   --> Translated Q and A
   ![image](https://github.com/user-attachments/assets/27105d92-5914-40ed-b2bf-43924f397814)

   
   **Faq-List**

   --> FAQ list is open by using this url :  curl http://localhost:8000/faq_app/faq-list/
   ![image](https://github.com/user-attachments/assets/527a2977-28d5-4a4b-88cb-5973ddc79f4c)


   **User added FAQS**
   
   --> User can Sumbit FAQ by using this url : curl http://localhost:8000/faq_app/submit/
   ![image](https://github.com/user-attachments/assets/3799bf14-2032-4ed1-9581-98068d2a5b5b)

   --> Updated FAQS 
   ![image](https://github.com/user-attachments/assets/c0b32f42-a42e-4837-9b7d-4acbc447d2ac)

   **multilingual support** 
   
   --> Select language(en, hi, bn) by using this url : curl http://localhost:8000/faq_app/faq-list/?lang=hi
   ![image](https://github.com/user-attachments/assets/4e742c05-9fe7-4eb6-8ec5-dbe8f4e91298)


**3) Unit testing is done(using pytest)**
   
   1) API testing on 1) faqlist with lang parameter, submit_faq, faq_list
      
   2) model testing on 1) faq_creation 2) faq_translation
   ![image](https://github.com/user-attachments/assets/bf9ee7ad-cc5a-4336-9423-0b48bacba0be)

**4) Connected the Redis for cache**

   using this command docker run --name redis-container -p 6379:6379 -d redis, docker ps
![image](https://github.com/user-attachments/assets/d0da5b77-7060-4658-a0ee-bf1c04113c09)







   






