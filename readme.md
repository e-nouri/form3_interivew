This is a repo for the form3 technical interivew.

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
 
    `id=[integer]`

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
    requests.get("api/payments/1234656")
  ```

---

**Create Payment**
----
  Payments API.

* **URL**

  /payments/

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
    `id=[integer]`

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
    requests.get("api/payments/1234656")
  ```