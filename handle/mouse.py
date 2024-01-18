import time

from selenium.webdriver.common.action_chains import ActionChains


def slow_scroll_and_close(self):
    bot = self.bot

    bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    actions = ActionChains(bot)

    actions.move_by_offset(0, 5).perform()
    time.sleep(0.1) 




