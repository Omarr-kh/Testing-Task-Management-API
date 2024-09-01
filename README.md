# Testing-Task-Management-API


# **API Documentation**

## **Base URL**
`/api/tasks/`

## **Authentication**
- All endpoints require the user to be authenticated.
- The user must be logged in to create, update, or delete tasks.

---

## **Endpoint: List and Create Tasks**

- **URL:** `/api/tasks/`
- **Method:** `GET`, `POST`
- **Authentication Required:** Yes

### **List Tasks (GET)**
- **Description:** Retrieves a list of tasks associated with the authenticated user.
  
#### **Request:**
- **Headers:**
  - `Authorization: Token <token>`

#### **Response:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`
  
```json
[
    {
        "id": 1,
        "title": "Task Title 1",
        "description": "Task Description 1",
        "status": false
    },
    {
        "id": 2,
        "title": "Task Title 2",
        "description": "Task Description 2",
        "status": true
    }
]
```

### **Create Task (POST)**
- **Description:** Creates a new task for the authenticated user.
  
#### **Request:**
- **Headers:**
  - `Authorization: Token <token>`
  - `Content-Type: application/json`
  
- **Body:**
  ```json
  {
      "title": "New Task Title",
      "description": "New Task Description"
  }
  ```

#### **Response:**
- **Status Code:** `201 Created`
- **Content-Type:** `application/json`
  
```json
{
    "id": 3,
    "title": "New Task Title",
    "description": "New Task Description",
    "status": false
}
```

#### **Error Responses:**
- **Status Code:** `400 Bad Request` (e.g., missing required fields)
  
```json
{
    "title": [
        "This field is required."
    ]
}
```

---

## **Endpoint: Retrieve, Update, and Delete a Task**

- **URL:** `/api/tasks/<int:id>/`
- **Method:** `GET`, `PUT`, `DELETE`
- **Authentication Required:** Yes

### **Retrieve Task (GET)**
- **Description:** Retrieves details of a specific task.
  
#### **Request:**
- **Headers:**
  - `Authorization: Token <token>`

#### **Response:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`
  
```json
{
    "id": 1,
    "title": "Task Title 1",
    "description": "Task Description 1",
    "status": false
}
```

#### **Error Responses:**
- **Status Code:** `404 Not Found` (e.g., task does not exist)
  
```json
{
    "detail": "Not found."
}
```

### **Update Task (PUT)**
- **Description:** Updates a specific task's details.
  
#### **Request:**
- **Headers:**
  - `Authorization: Token <token>`
  - `Content-Type: application/json`
  
- **Body:**
  ```json
  {
      "title": "Updated Task Title",
      "description": "Updated Task Description",
      "status": true
  }
  ```

#### **Response:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`
  
```json
{
    "id": 1,
    "title": "Updated Task Title",
    "description": "Updated Task Description",
    "status": true
}
```

#### **Error Responses:**
- **Status Code:** `400 Bad Request` (e.g., invalid data)
  
```json
{
    "title": [
        "This field is required."
    ]
}
```
- **Status Code:** `403 Forbidden` (e.g., user not authorized to update the task)

```json
{
    "detail": "You do not have permission to perform this action."
}
```

- **Status Code:** `404 Not Found` (e.g., task does not exist)
  
```json
{
    "detail": "Not found."
}
```

### **Delete Task (DELETE)**
- **Description:** Deletes a specific task.
  
#### **Request:**
- **Headers:**
  - `Authorization: Token <token>`

#### **Response:**
- **Status Code:** `204 No Content`

#### **Error Responses:**
- **Status Code:** `403 Forbidden` (e.g., user not authorized to delete the task)

```json
{
    "detail": "You do not have permission to perform this action."
}
```
- **Status Code:** `404 Not Found` (e.g., task does not exist)
  
```json
{
    "detail": "Not found."
}
```

---

## **Manual Testing Instructions**

### **Using Postman**

1. **Authentication:**
   - Use the login endpoint to authenticate and get the token.
   - Set the `Authorization` header with the token in your requests.

2. **List Tasks (GET):**
   - Set the method to `GET`.
   - Set the URL to `/api/tasks/`.
   - Add the `Authorization` header.
   - Click "Send" to retrieve the list of tasks.

3. **Create Task (POST):**
   - Set the method to `POST`.
   - Set the URL to `/api/tasks/`.
   - Add the `Authorization` header.
   - Set the `Content-Type` to `application/json`.
   - Provide the `title` and `description` fields in the request body.
   - Click "Send" to create a new task.

4. **Update Task (PUT):**
   - Set the method to `PUT`.
   - Set the URL to `/api/tasks/<task_id>/`.
   - Add the `Authorization` header.
   - Set the `Content-Type` to `application/json`.
   - Provide the updated `title`, `description`, and `status` fields in the request body.
   - Click "Send" to update the task.

5. **Delete Task (DELETE):**
   - Set the method to `DELETE`.
   - Set the URL to `/api/tasks/<task_id>/`.
   - Add the `Authorization` header.
   - Click "Send" to delete the task.

### **Using curl**

1. **List Tasks:**
   ```bash
   curl -H "Authorization: Token <token>" -X GET http://<base_url>/api/tasks/
   ```

2. **Create Task:**
   ```bash
   curl -H "Authorization: Token <token>" -H "Content-Type: application/json" -X POST -d '{"title":"New Task", "description":"New Description"}' http://<base_url>/api/tasks/
   ```

3. **Update Task:**
   ```bash
   curl -H "Authorization: Token <token>" -H "Content-Type: application/json" -X PUT -d '{"title":"Updated Task", "description":"Updated Description", "status":true}' http://<base_url>/api/tasks/<task_id>/
   ```

4. **Delete Task:**
   ```bash
   curl -H "Authorization: Token <token>" -X DELETE http://<base_url>/api/tasks/<task_id>/
   ```

### **Testing Invalid Requests**

- **Create Task with Missing Fields:**
  - Remove either `title` or `description` from the POST request body and observe the `400 Bad Request` response.
  
- **Update Task with Invalid Data:**
  - Provide incorrect data types (e.g., boolean instead of string) for fields in the PUT request body to trigger validation errors.
  
- **Delete Nonexistent Task:**
  - Attempt to delete a task with an invalid `task_id` and observe the `404 Not Found` response.

