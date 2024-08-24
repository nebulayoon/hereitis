# ERD

```mermaid
erDiagram
"users"{
  UUID id PK
  Text name
  Text email
  Text password
  Timestamptz created_at
}

"contents"{
  UUID id PK
  Text type "TEXT, FILE"
  Text data
  Bool llm_status
  UUID user_Id FK
}

"contents" }o--|| "users" :memo
```