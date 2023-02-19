It solves 2 primary problems:
1. When a naive patient can just describe what he is feeling and still be able to find the best suited doctor for him
2. Maintain an e-record of all patient history so that a person can switch doctors without the hassle of describing his old routines

As for our first objective, we have a chatbot-based approach for the patient to input what all symptoms he is facing and get the nearest doctor to him that specializes in the problems he described. So, on the backend, a probable disease is predicted from the symptoms and then the doctor specialist is determined. The for selecting the best doctor, we have taken the data for patient ratings of doctors. So when we input the location and specialisation of the doctor to the recommendation system, it lists the best doctors.
As for our second objective, we aimed at digitalizing all the healthcare records that a patient might have. As of today, all doctors diagnose and prescribe medicines in a file by writing on a paper. This poses a difficulty to the patient when he has to consult another doctor. Also, a layman is generally unaware of the medical terms that a doctor may use. So if he has a e-record of his history, he would be able to directly show it to the new doctor and the new doctor would be able to treat the patient better. For this, we tried to develop a method in which the user can simply scan his prescription and our algorithm will find the text, recognise it and classify it into diagnosis and prescription of medicines (was difficult to implement).

### **Created Recommendation System API and tested using Postman**
![image](https://user-images.githubusercontent.com/70468773/219872848-05110427-225a-438b-ae6f-09cd665480f2.png)
