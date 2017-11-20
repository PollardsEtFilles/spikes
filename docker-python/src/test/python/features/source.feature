Feature: Source
  Access environment variables in Unix shell files in Python

  Scenario Outline: Read a shell file into a Source class
    Given a shell <file>
    When I read the file
    Then Source.<prop> should equal <expected>

    Examples:
      | file         | prop       | expected   |
      | env/env.sh   | atestenv   | some env   |
      | env/env.sh   | atestenv2  | some env2  |
