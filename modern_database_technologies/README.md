# US Walkability Database

## 🚀 Project Overview
This repository presents the development of a relational database for evaluating walkability and transit accessibility across cities in the United States. The database is designed to support travel agencies and users seeking accommodations with excellent walkability and transit options.

## 🎯 Objective
To create a database schema that models relationships between states, cities, hotels, airports, and their respective walk and transit scores. The database will serve as the backend for future applications using API integrations to retrieve and update walkability and transit scores.

---

## 📊 Key Features
- **Entities and Relationships**:
  - **State**: Each state contains multiple cities.
  - **City**: Associated with hotels, airports, and walk/transit scores.
  - **Hotel**: Each hotel is linked to a walk score and potentially a transit score.
  - **Airport**: Linked to a transit score if available.
  - **Scores**:
    - Walk Score: Indicates walkability of a hotel.
    - Transit Score: Indicates public transit accessibility for hotels and airports.
- **Business Rules**:
  - Hotels are limited to a maximum of 100 per city.
  - Scores are normalized and categorized in intervals of 10 (e.g., 20, 30, 40).
  - Queries allow insights like average city walk scores or identifying states with poor walkability.

---

## 🛠️ Methodology
1. **Conceptual Data Modeling**:
   - Entity-Relationship Diagram (ERD) defining all entities, attributes, and primary keys.
   - Established constraints to ensure data integrity and compliance with business rules.
2. **Logical Data Modeling**:
   - Relationships resolved to 3NF for normalization.
   - Designed for implementation in Microsoft SQL Server.
   - Optimized with separate `Location` table for latitude and longitude data.
3. **Database Implementation**:
   - SQL scripts for:
     - Data Definition Language (DDL): Table creation and schema setup.
     - Data Manipulation Language (DML): Insertions for states, cities, hotels, airports, and scores.
     - Data Query Language (DQL): Queries to support common user requests.
4. **API Integration Readiness**:
   - Database designed to support API calls for walk and transit scores.

---

## 🌟 Results
- **Implemented Queries**:
  - Average walk score of hotels in a city.
  - Identification of hotels with very walkable scores (70+).
  - Cities with decent public transit at hotels and airports (scores 50+).
  - States with low walk and transit scores.
- **Scalability**:
  - Ready for integration with APIs for automated data fetching and updates.
  - Future improvements include adjusting latitude/longitude precision and dynamic data updates.

---
