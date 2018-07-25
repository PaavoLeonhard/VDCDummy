# VDCDummy

Readme

VDC mock up implementation for OSR use case of the DITAS project


to start use following commands
- docker build .
- docker run -p 8000:8000 [container-ID]

The service creates mock-up data. It enables the user to simulate errors or higher latency on the server side.
More search parameters in the GET query result in less data returned.

Possible behaviour parameter can be transmitted as form-data or Json body 
- no_response: The server won't respond to GET request(if True)
- wait_timed: The server waits the amount of time specified (in sec) 
- error_rate: The server returns a 500 error according to the rate (80 means 80 percent of the time)
- data_reduction: Data is reduced by the factor given



### API:
| Method | Path               | Details                      | Returns 
| :--- | :---| --- | --- | 
| GET    | /patient?     | ssn, patientid, try, chol, hep, date| Patient | |
| GET    | /exam?        | ssn, patientid, try, chol, hep, date | \[Exam,...\] | |
| GET    | /find?...          | ssn, patientid, try, chol, hep, date|  \[Exam,...\]||
| POST    | /behaviour/     | no_response= "True" or "False", wait_time=integer, error_rate=0-100, data_reduction=0-3000 | HttpResponse |





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
