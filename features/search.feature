@regression
@smoke
Feature: Search

    @regression
    @smoke
    Scenario Outline: Search behave
        Given I navigate to the baidu Home page
        When I search for "<search_term>"
        Then I am taken to the "<search_term>" Search Results page
        And I see a search result "<search_result>"



        Examples:
        | search_term | search_result |
        | behave      | behave · PyPI |
        | selenium    | Selenium automates browsers. That's it! |