android_desired_caps = {
    "build": "Python Android",
    'device': 'Google Pixel',
    'os_version': '7.1',
    'appPackage': 'com.auth0.samples',
    'appActivity': 'com.auth0.samples.MainActivity',
    'app': 'Auth0',
    'chromeOptions': {
        'androidPackage': 'com.android.chrome'
    }
}
android_desired_caps_emulator = {
    'platformName': 'android',
    'deviceName': 'Nexus_6p',
    'appPackage': 'com.auth0.samples',
    'appActivity': 'com.auth0.samples.MainActivity',
    'chromeOptions': {
        'androidPackage': 'com.android.chrome'
    }
}

ios_desired_caps = {
    "platformName": "iOS",
    "platformVersion": "11.0",
    "deviceName": "iPhone 7",
    "automationName": "XCUITest",
    "app": "/path/to/my.app"
}

login_user = "asdasd"
login_password = "asdasd"

