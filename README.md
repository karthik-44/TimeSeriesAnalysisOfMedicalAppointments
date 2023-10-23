# TimeSeriesAnalysisOfMedicalAppointments
### Project Description
The "Healthcare Appointments Analytics" project is a comprehensive data analysis initiative that delves into the intricacies of medical appointments and explores factors influencing patient attendance and no-show rates. By leveraging advanced analytical techniques, the project aims to uncover valuable insights that can positively impact patient engagement and resource allocation in healthcare settings.

### Overview:
- Read the raw data using pandas and create a dataframe.
- Check for duplicates, null values and take necessary actions.
- Appropriate data type conversion for the columns.
- Creating new feature(s) as required from the given dataset.
- Drop unnecessary columns from the dataframe and export the dataset as a .csv file.
- Use the exported dataset to create a database and use SQL to extract insights using any SQL client (MySQL Workbench).
- Used jupyter notebook to show the results as it is easy to share and visualize the code and output.

## Module 1

1. Read the patients data from Hospital_patients_datasets.csv file.
2. Check for the duplicates and null values in the dataset.
3. Convert the data types of the columns properly. For eg: ScheduledDay, AppointmentDay to datetime.
4. Rename the columns as per the python dictionary: 
{'Hipertension' : 'Hypertension', 
                   'Handcap' : 'Handicap',
                   'SMS_received' : 'SMSReceived', 
                   'No-show' : 'NoShow'}

## Module 2

1. Drop the columns which are not used for our analysis - 'PatientId', 'AppointmentID', 'Neighbourhood'.
2. Convert the age column into age bins of size 20.
3. Clean and export the dataset as patients.csv and download it.
4. Use the database details, login and import the file patients.csv into the database.

At this point we have our data sources from which we can query the information based on our analysis questions.

## Module 3

### Task 1. How many values are there in the given dataset?
There are **106987** rows in the dataset.

### Task 2. Count the number of appointments for each day in the given dataset:

| AppointmentDay | n_appointments |
|--------------- | --------------- |
|   2016-04-29   |      3,104      |
|   2016-05-02   |      4,214      |
|   2016-05-03   |      4,129      |
|   2016-05-04   |      4,048      |
|   2016-05-05   |      4,113      |
|   2016-05-06   |      3,791      |
|   2016-05-09   |      4,352      |
|   2016-05-10   |      4,177      |
|   2016-05-11   |      4,347      |
|   2016-05-12   |      4,233      |
|   2016-05-13   |      3,885      |
|   2016-05-14   |        39       |
|   2016-05-16   |      4,449      |
|   2016-05-17   |      4,227      |
|   2016-05-18   |      4,220      |
|   2016-05-19   |      4,109      |
|   2016-05-20   |      3,707      |
|   2016-05-24   |      3,876      |
|   2016-05-25   |      3,768      |
|   2016-05-30   |      4,360      |
|   2016-05-31   |      4,158      |
|   2016-06-01   |      4,351      |
|   2016-06-02   |      4,204      |
|   2016-06-03   |      3,978      |
|   2016-06-06   |      4,528      |
|   2016-06-07   |      4,264      |
|   2016-06-08   |      4,356      |


### Task 3. Calculate the average number of appointments (Set to nearest whole number) per day in the given dataset

The average number of appointments per day is **3962**

### Task 4. Find the day with the highest number of appointments in the given dataset.

**June 06,2016** is the day with the highest number of appointment - **4528**.

### Task 5. Calculate the monthly average number of appointments in the given dataset.

| appointment_month | n_appointments |
|------------------ | --------------- |
|     2016-04      |      3,104      |
|     2016-05      |     78,202      |
|     2016-06      |     25,681      |


### Task 6. Find the month with the highest number of appointments in the given dataset.

The month with the highest number of appointments is **May of 2016** with **78202** number of appointments.

### Task 7. Calculate the weekly average number of appointments in the given dataset.

|  year  | week | n_appointments_week |
|------- |------|--------------------|
|  2016  |  17  |        3,104        |
|  2016  |  18  |       20,295        |
|  2016  |  19  |       21,033        |
|  2016  |  20  |       20,712        |
|  2016  |  21  |        7,644        |
|  2016  |  22  |       21,051        |
|  2016  |  23  |       13,148        |

### Task 8. Find the week with the highest number of appointments in the given dataset.

|  year  | week | n_appointments_week |
|------- |------|--------------------|
|  2016  |  22  |        21,051       |


### Task 9. What is the distribution of appointments based on gender in the dataset?

| gender | n_appointments |
|--------|---------------|
|   F    |     70,118    |
|   M    |     36,869    |


### Task 10. Calculate the number of appointments per weekday in the given dataset.

|   weekday  | n_appointments |
|-----------|---------------|
|   Friday   |     18,465     |
|  Tuesday  |     24,831     |
|   Monday |     21,903     |
| Wednesday |    25,090     |
| Thursday  |     16,659     |
| Saturday  |        39        |


### Task 11. Calculate the average time between scheduling and the appointment day in the given dataset.

The average time between scheduling and the appointment day is **10 days**.
