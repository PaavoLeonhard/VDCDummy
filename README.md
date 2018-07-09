# VDCDummy

Readme

VDC mock up implementation for OSR use case of the DITAS project


to start use following commands
- virtualenv -p python3 djangodev
- python manage.py runserver

The service creates mock-up data. It enables the user to simulate errors or higher latency on the server side.
More search parameters in the GET query result in less data returned.

no_response: The server won't respond to GET request(if True)
wait_timed: The server waits the amount of time specified (in sec) 
error_rate: The server returns a 500 error according to the rate (80 means 80 percent of the time)
data_reduction: Data is reduced by the factor given


### API:
| Method | Path               | Details                      | Returns | Body or Form
| :--- | :---| --- | --- | --- |
| GET    | /patient?     | ssn, patientid, try, chol, hep, date| Patient | |
| GET    | /exam?        | ssn, patientid, try, chol, hep, date | \[Exam,...\] | |
| GET    | /find?...          | ssn, patientid, try, chol, hep, date|  \[Exam,...\]||
| GET    | /behaviour/     |  | HttpResponse |no_response= "True" or "False", wait_time=integer, error_rate=0-100, data_reduction=0-3000 |





Patient:
```
{
  "SSN": 0,
  "lastName": "string",
  "name": "string",
  "gender": "male",
  "mail": "user@example.com",
  "birthday": "string"
}
```

Exam:
```
  {
    "SSN": 0,
    "lastName": "string",
    "name": "string",
    "date": "2017-11-28T16:36:57.713Z",
    "cholesterol": 0,
    "triglyceride": 0,
    "hepatitis": true
  }
```
