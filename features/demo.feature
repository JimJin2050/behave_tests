Feature: DEMO testing

  @demo
  Scenario Outline: for http api testing
    Given request type is <request_type>
    When I input HTTP api <url> and <parametes>
    Then The status code is 200

   Examples: all request type
    |request_type|url                    |parametes|
    |get         |https://www.baidu.com/s|{'wd':'python','rn':'3'}|
    |get         |https://www.baidu.com/s|{'wd':'restful api','rn':'3'}|
    |get         |https://www.baidu.com/s|{}                      |
