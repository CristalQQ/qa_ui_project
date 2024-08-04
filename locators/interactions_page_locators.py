class SortablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    TAB_LIST_ITEMS = ("xpath", "//div[@id='demo-tabpane-list']//div[@class='list-group-item list-group-item-action']")
    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    TAB_GRID_ITEMS = ("xpath", "//div[@id='demo-tabpane-grid']//div[@class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    TAB_LIST_ITEMS = (
        "xpath", "//ul[@id='verticalListContainer']/li[@class='mt-2 list-group-item list-group-item-action']"
    )
    TAB_LIST_ACTIVE_ITEMS = (
        "xpath", "//ul[@id='verticalListContainer']/li[@class='mt-2 list-group-item active list-group-item-action']"
    )

    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    TAB_GRID_ITEMS = ("xpath", "//div[@id='demo-tabpane-grid']//li[@class='list-group-item list-group-item-action']")
    TAB_GRID_ACTIVE_ITEMS = (
        "xpath", "//div[@id='demo-tabpane-grid']//li[@class='list-group-item active list-group-item-action']"
    )