# basic user configuration machine built on code academy required to complete prior to getting certificate

def add_setting(setting, new_setting):
    key = str(new_setting[0])
    value = str(new_setting[1])
    if key.lower() in setting:
        return f"Setting '{key.lower()}' already exists! Cannot add a new setting with this name."
    else: 
        setting.update({key.lower() : value.lower()})
        return f"Setting '{key.lower()}' added with value '{value.lower()}' successfully!"



def update_setting(setting, new_setting):
    key = str(new_setting[0])
    key = key.lower()
    value = str(new_setting[1])
    value = value.lower()
    if key in setting:
        setting.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(setting, key):
    key = key.lower()
    if key in setting:
        del setting[key]
        return f"Setting '{key.lower()}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(setting):
    if len(setting) == 0:
        return "No settings available."
    else:
        total_string = "Current User Settings:\n"
        for key,value in setting.items():
            total_string += f"{key.capitalize()}: {value}\n"
        return total_string


test_settings = {}
add_setting(test_settings, ('Theme', 'dark'))
add_setting(test_settings, ('VOLUME', 'low'))
add_setting(test_settings, ('Notifications', 'disabled'))
print(view_settings(test_settings))
update_setting(test_settings, ('ThEme', 'light'))
update_setting(test_settings, ('Volume', 'HIGH'))
update_setting(test_settings, ('Notifications', 'enabled'))
print(view_settings(test_settings))
delete_setting(test_settings,'Theme')
print(view_settings(test_settings))




