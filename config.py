# android_desired_caps = {
#     "build": "Python Android",
#     "device": "Google Pixel",
#     "app": "bs://<hashed app-id>"
# }
android_desired_caps = {
    "build": "Python Android",
    'device': 'Google Pixel',
    'os_version': '8.0',
    'appPackage': 'com.auth0sample',
    'appActivity': 'com.auth0sample.MainActivity',
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

# userName = "3lb3njy"
# accessKey = "7978fef9-72c6-4fcc-bf32-d22581550349"

userName = "benjaminlizardo2"
accessKey = "2SP8isyH9azrD1sSsiCJ"