# Moupegnou Nzoussi kevin Grace
Задача: спроектировать и разработать API для системы опросов пользователей

## Installation requirements
  * python3.7
  * Django2.2.10
  * djangorestframework3.11.0

## Installation guide
  ```
  cd pollMaker/
  pip install -r requirements.txt
  cd pollMaker/
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```

## API documentation
### To get user token: 
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body: 
    * username: 
    * password: 
* Example:
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

### To create poll:
* Request method: POST
* URL: http://localhost:8000/api/poll/create/
* Header:
   *  Authorization: Token userToken
* Body:
    * poll_name: name of poll
    * pub_date: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    * end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
    * Poll_description: description of poll
* Example: 
```
curl --location --request POST 'http://localhost:8000/api/poll/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'pub_date=%pub_date' \
--form 'end_date=%end_date \
--form 'poll_description=%poll_description'
```

### To update poll:
* Request method: PATCH
* URL: http://localhost:8000/api/poll/update/[poll_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id 
* Body:
    * poll_name: name of poll
    * end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
    * Poll_description: description of poll
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'end_date=%end_date \
--form 'poll_description=%poll_description'
```

### To delete poll:
* Request method: DELETE
* URL: http://localhost:8000/api/poll/update/[poll_id]
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
Example:
```
curl --location --request DELETE 'http://localhost:8000/api/poll/update/[poll_id]/' \
--header 'Authorization: Token %userToken'
```

### To view all polls:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/' \
--header 'Authorization: Token %userToken'
```

### To view currently active polls:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/active/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/poll/view/active/' \
--header 'Authorization: Token %userToken'
```

### To create question:
* Request method: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll 
    * question_text: 
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To update question:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * poll: id of poll 
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To delete question:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### To create choice:
* Request method: POST
* URL: http://localhost:8000/api/choice/create/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To update choice:
* Request method: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To delete choice:
* Request method: DELETE
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### To create answer:
* Request method: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### To update answer:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * poll: id of poll
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### To delete answer:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### To view answers of user:
* Request method: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
```

  
