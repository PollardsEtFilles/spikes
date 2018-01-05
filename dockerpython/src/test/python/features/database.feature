Feature: Database

  Scenario: Create a database connection
    Given a "employees" database on host "db" user "root" passwd "password"
    When a client connects
    And the "employees.sql" database is imported from "/code/test_db-master" with "/code/.my.cnf"
    Then there is some data in the "employees" table
