import yaml
import logging
root_log=logging.getLogger()
logging.basicConfig(level=logging.INFO)
def test_yaml():
    logging.info("test_yaml")
    pythonobj={'desirecaps': {'platformName': 'android', 'deviceName': 'mumu_test01', 'appPackage': 'com.tencent.wework', 'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'true', 'skipServerInstallation': 'true', 'skipDeviceInitialization': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    # print(yaml.safe_dump(pythonobj))
    logging.info(yaml.safe_dump(pythonobj))