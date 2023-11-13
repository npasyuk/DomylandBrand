import pexpect

from create_brand_feature.env import root_project_directory


def create(app_key):
    keystore_path = f"{root_project_directory}/{app_key}.jks"
    keystore_password = "reHuIdd123"
    key_alias = f"{app_key}"
    key_password = "reHuIdd123"
    first_name = "DML"
    last_name = "Creator"
    org_unit = "IT Department"
    org_name = "Domyland"
    locality = "Moscow"
    state = "Moscow"
    country = "RU"

    # Run the keytool command
    # command = f"keytool -genkey -v -keystore {{}} -keyalg RSA -keysize 2048 -validity 10000 -alias {key_alias}"
    newCommand = f"keytool -genkeypair -alias {key_alias} -keyalg RSA -keystore {keystore_path} -keysize 2048 -validity 10000 -keypass {key_password} -storepass {keystore_password}"
    keytool = pexpect.spawn(
        newCommand.format(
            keystore_path), encoding='utf-8')

    # Wait for the prompts and input the values
    keytool.expect("What is your first and last name?")
    keytool.sendline("{} {}".format(first_name, last_name))
    keytool.expect("What is the name of your organizational unit?")
    keytool.sendline(org_unit)
    keytool.expect("What is the name of your organization?")
    keytool.sendline(org_name)
    keytool.expect("What is the name of your City or Locality?")
    keytool.sendline(locality)
    keytool.expect("What is the name of your State or Province?")
    keytool.sendline(state)
    keytool.expect("What is the two-letter country code for this unit?")
    keytool.sendline(country)
    keytool.expect("CN={} {}.*".format(first_name, last_name))
    keytool.sendline("yes")
    keytool.expect(pexpect.EOF)

    # Print the output
    print(keytool.before)
