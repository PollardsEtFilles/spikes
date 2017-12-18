Feature: Pytest Database

  Scenario: Import a database
    Given a employees database on host db user root passwd password
    #Given a "employee" database on host "db" user "employee" passwd "password"
    When a client connects
    And the "employees.sql" database is imported from "/code/test_db-master" with "/code/.my.cnf"
    Then there is some data in the "employees" table
