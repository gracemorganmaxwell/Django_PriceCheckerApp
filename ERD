# NZ Price Checker Web App Relational Diagram

## Tables and Relationships

### SupermarketChain Table
- **id** (Primary Key)
- **name**

### Store Table
- **id** (Primary Key)
- **name**
- **address**
- **region**
- **chain_id** (Foreign Key references `SupermarketChain(id)`)

### Product Table
- **id** (Primary Key)
- **name**
- **image**
- **unit_type**
- **store_id** (Foreign Key references `Store(id)`)
- **product_code** (Unique)
- **unit_price**
- **on_sale**

### PriceHistory Table
- **id** (Primary Key)
- **product_id** (Foreign Key references `Product(id)`)
- **price**
- **date**
- **on_sale**

### User Table
- **id** (Primary Key)
- **username** (Unique)
- **password**
- **email** (Unique)
- **name**
- **user_type**

### UserStorePreference Table
- **id** (Primary Key)
- **user_id** (Foreign Key references `User(id)`)
- **store_id** (Foreign Key references `Store(id)`)

## Relationships Overview

```plaintext
SupermarketChain (1) ---- (∞) Store
     |                        |
     |                        |
     |                        |
    (∞)                      (∞)
   Store                   Product
                             |
                             |
                            (∞)
                        PriceHistory

User (1) ---- (∞) UserStorePreference ---- (∞) Store
```

### Description of Relationships

1. **SupermarketChain** has a one-to-many relationship with **Store**.
   - Each supermarket chain can have multiple stores.
   - Each store is linked to one supermarket chain.

2. **Store** has a one-to-many relationship with **Product**.
   - Each store can offer multiple products.
   - Each product is linked to a specific store.

3. **Product** has a one-to-many relationship with **PriceHistory**.
   - Each product can have multiple historical price records.
   - Each price history entry is associated with one product.

4. **User** has a many-to-many relationship with **Store** through the `UserStorePreference` table.
   - Each user can prefer multiple stores.
   - Each store can be preferred by multiple users.


### Explanation

- **Tables**: Each table is defined with its respective attributes. Primary keys and foreign keys are noted, as well as unique constraints.
- **Relationships**: The relationships between tables are depicted using plain text and ASCII art, showing how the entities (tables) connect with each other.
- **Explanation**: Each relationship is briefly explained to clarify the nature of the connections between the tables.
