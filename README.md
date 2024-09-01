# Testing-Task-Management-API


# **API Documentation**

## **Base URL**
`/api/tasks/`

## **Endpoint: List and Create Tasks**

- **URL:** `/api/tasks/`
- **Method:** `GET`, `POST`

### **List Tasks (GET)**
- **Description:** Retrieves a list of tasks.
  
#### **Request:**
- **Url:**
  - `/api/tasks`

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
- **Description:** Creates a new task.
  
#### **Request:**
- **Headers:**
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

- **Status Code:** `404 Not Found` (e.g., task does not exist)
  
```json
{
    "detail": "Not found."
}
```

### **Delete Task (DELETE)**
- **Description:** Deletes a specific task.

#### **Response:**
- **Status Code:** `204 No Content`

#### **Error Responses:**

- **Status Code:** `404 Not Found` (e.g., task does not exist)
  
```json
{
    "detail": "Not found."
}
```

---

## **Manual Testing Instructions**

### **Using Postman**

1. **List Tasks (GET):**
   - Set the method to `GET`.
   - Set the URL to `/api/tasks/`.
   - Click "Send" to retrieve the list of tasks.

2. **Create Task (POST):**
   - Set the method to `POST`.
   - Set the URL to `/api/tasks/`.
   - Set the `Content-Type` to `application/json`.
   - Provide the `title` and `description` fields in the request body.
   - Click "Send" to create a new task.

3. **Update Task (PUT):**
   - Set the method to `PUT`.
   - Set the URL to `/api/tasks/<task_id>/`.
   - Set the `Content-Type` to `application/json`.
   - Provide the updated `title`, `description`, and `status` fields in the request body.
   - Click "Send" to update the task.

4. **Delete Task (DELETE):**
   - Set the method to `DELETE`.
   - Set the URL to `/api/tasks/<task_id>/`.
   - Click "Send" to delete the task.


### **Testing Invalid Requests**

- **Create Task with Missing Fields:**
  - Remove either `title` or `description` from the POST request body and observe the `400 Bad Request` response.
  
- **Update Task with Invalid Data:**
  - Provide incorrect data types (e.g., boolean instead of string) for fields in the PUT request body to trigger validation errors.
  
- **Delete Nonexistent Task:**
  - Attempt to delete a task with an invalid `task_id` and observe the `404 Not Found` response.

