from appium import webdriver
from config import *
from browserstack import *
from os_enum import OSEnum


class Driver:

    def __init__(self, os_type: OSEnum):
        if os_type == OSEnum.ANDROID:
            print(run_is_local)
            if run_is_local:
                self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                                 android_desired_caps_emulator)
            else:
                self.instance = webdriver.Remote("http://" + userName + ":" + accessKey +
                                                 "@hub-cloud.browserstack.com/wd/hub",
                                                 android_desired_caps)
        elif os_type == OSEnum.IOS:
            if run_is_local:
                self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", ios_desired_caps)
            else:
                self.instance = webdriver.Remote("http://" + userName + ":" + accessKey +
                                                 "@hub-cloud.browserstack.com/wd/hub",
                                                 ios_desired_caps)


