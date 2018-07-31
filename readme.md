This is a repo for the form3 technical interivew.

The endpoint /payments acceptes: ['GET', 'POST'] <br />
The endpoint /payments/:id acceptes: ['GET', 'PATCH', 'PUT', 'DELETE']

---

REST API Documentation:
=======================


**Request all Payment**
----
  Payments API.

* **URL**

  /payments/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**

    None

* **Data Params**
  
    None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "out of range parameters." }`

* **Sample Call:**

  ```python
    requests.get("api/payments/1234656")
  ```

---

**Request Payment with ID**
----
  Payments API.

* **URL**

  /payments/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
    `id=[uuid]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```python
    requests.get("api/payments/743d5b63-8e6f-432e-a8fa-c5d8d2ee5fcb")
  ```

---

**Create a Payment**
----
  Create a Payment object.

* **URL**

  /payments/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
    None

* **Data Params**

    ``` yaml
    type:
        # This can be hardcoded because it is payment endpoin, or droped
        type: string
        required: true
    id:
        type: uuid
        required: true
        # This shoulw be the unique key
        # Because of the version, the unique key should be the (id, versuon)
        # for the sake of simplicity I will use this as the unique key
        unique: true
    version:
        # This can be hardcoded because it is good practice to keep
        # all versions in source control (git) as seperat files
        type: number
        required: true
    organisation_id:
        type: uuid
        required: true
    attributes:
        type: dict
        # This is because I am not detailing all of the fields here
        allow_unknown: true
        required: true
    ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```python
    requests.post("api/payments/", body)
  ```

---

**Delete a Payment**
----

  Delete a Paymentwith its uuid.

* **URL**

  /payments/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
    `id=[uuid]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```python
    requests.get("api/payments/743d5b63-8e6f-432e-a8fa-c5d8d2ee5fcb")
  ```

---

**Update a Payment**
----
  Update a Payment object with its UID.
  About the Update, the Patch method can be requested with one of the feilds, all of them are not required together, only the direred field have to be sent with the new value to be updated.
* **URL**

  /payments/:id

* **Method:**

  `PATCH`
  
*  **URL Params**

   **Required:**
 
    `id=[uuid]`

* **Data Params**

    ``` yaml
    type:
        # This can be hardcoded because it is payment endpoin, or droped
        type: string
        required: false
    organisation_id:
        type: uuid
        required: false
    attributes:
        type: dict
        # This is because I am not detailing all of the fields here
        allow_unknown: true
        required: false
    ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```python
    requests.post("api/payments/", body)
  ```


**Replace a Payment**
----
  Replace a Payment object.

* **URL**

  /payments/:id

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
    `id=[uuid]`

* **Data Params**

    ``` yaml
    type:
        # This can be hardcoded because it is payment endpoin, or droped
        type: string
        required: true
    version:
        # This can be hardcoded because it is good practice to keep
        # all versions in source control (git) as seperat files
        type: number
        required: true
    organisation_id:
        type: uuid
        required: true
    attributes:
        type: dict
        # This is because I am not detailing all of the fields here
        allow_unknown: true
        required: true
    ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```python
    requests.put("api/payments/", body)
  ```