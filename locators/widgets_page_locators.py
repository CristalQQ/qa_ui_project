class AccordianPageLocators:
    CARD_FIRST = ("xpath", "//div[@id='section1Heading']")
    CARD_FIRST_COLLAPSE_STATUS = ("xpath", "//div[@id='section1Heading']/following-sibling::div[@class]")
    CARD_FIRST_TEXT = ("xpath", "//div[@id='section1Content']/p")
    CARD_SECOND = ("xpath", "//div[@id='section2Heading']")
    CARD_SECOND_COLLAPSE_STATUS = ("xpath", "//div[@id='section2Heading']/following-sibling::div[@class]")
    CARD_SECOND_TEXT = ("xpath", "//div[@id='section2Content']/p")


