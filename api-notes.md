# What is an API?

**API** stands for **Application Programming Interface**.

In simple terms, an API is a **way for two software applications to communicate with each other**.

### Simple Example

```text
Your App
   ↓
   ↓
Server / Database
   ↓
  API
   ↓
Your App
```

The app sends a **request** to the API, and the API sends back a **response**.

---

## 🍔 Simple Analogy

Think about a restaurant:

* **Customer** → Requests food
* **Waiter** → Takes the order and brings the food
* **Kitchen** → Prepares the food

Here, the **waiter acts like an API**.

The customer does not need to go directly to the kitchen. The customer gives the request to the waiter, and the waiter communicates with the kitchen.

Similarly, an API acts as a **bridge between software applications**.

---

## Why are APIs Important?

APIs allow different applications and services to:

* Communicate with each other
* Send and receive data
* Share information
* Use services provided by other applications
* Build scalable applications

### Examples

* A weather app uses an API to get weather information.
* A payment app uses APIs to process payments.
* A food delivery app uses APIs to get restaurant and order information.
* A frontend application uses APIs to communicate with a backend.

---

## Real-World Example

Suppose an application wants to get the weather information for Delhi.

It sends a request:

```http
GET /weather/delhi
```

The API processes the request and returns a response:

```json
{
  "city": "Delhi",
  "temperature": 32,
  "condition": "Sunny"
}
```

The application can then display this information to the user.

---

## Request and Response

Most APIs work with a simple **request → response** model.

```text
Client
  ↓
Request
  ↓
API
  ↓
Server
  ↓
Response
  ↓
Client
```

* **Request** → What the client wants
* **Response** → What the server sends back

---

## API in One Line

> **An API is a bridge that allows different software applications to communicate and exchange data.**

---

# Monolithic vs Microservices Architecture

## Monolithic Architecture

A **monolithic application** is one large application where all the main features are part of the same codebase.

For example:

```text
Monolithic Application
│
├── Login
├── Users
├── Orders
├── Payments
└── Products
```

### Advantages

* Simple to start
* Easy to develop initially
* Easy to deploy

### Disadvantages

* Can become difficult to maintain as it grows
* Changes in one part can affect other parts
* Scaling individual features is difficult

---

## Microservices Architecture

A **microservices architecture** divides an application into many small, independent services.

Each service handles a specific job.

```text
Microservices
│
├── User Service
├── Order Service
├── Payment Service
└── Product Service
```

These services communicate with each other using APIs.

### Advantages

* Services can be developed separately
* Services can be deployed separately
* Individual services can be scaled
* Easier to manage large systems

### Disadvantages

* More complex to build
* Services need to communicate with each other
* Deployment and monitoring can be more difficult

---

## Simple Example

```text
Monolithic
→ One big application doing everything

Microservices
→ Many small services, each doing one job
```

---

## Monolithic vs Microservices

| Monolithic                         | Microservices                       |
| ---------------------------------- | ----------------------------------- |
| One large application              | Many small services                 |
| Simple to start                    | More complex                        |
| Single codebase                    | Multiple codebases/services         |
| Easier to deploy initially         | Services can be deployed separately |
| Harder to scale individual parts   | Easier to scale individual services |
| Good for small/simple applications | Good for large/complex applications |

---

## In Short

* **API** → Allows software to communicate.
* **Request** → Sent by the client.
* **Response** → Sent back by the server.
* **Monolithic** → One big application.
* **Microservices** → Many small independent services.
* **APIs** → Often used to connect microservices.

### Remember

```text
API = Communication between software systems
```
