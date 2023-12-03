# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
import streamlit as st


device_map = {
    'm': 'Mobile',
    'd': 'Desktop',
    't': 'Tablet'
}

sdk_map = {
    'andx': "Android Native SDK",
    'arnx': 'Android React Native SDK',
    'aflt': 'Android Flutter SDK',
    'acor': 'Android Cordova SDK',
    'acap': 'Android Capacitor SDK',
    'axmf': 'Android Xamarin Forms SDK',
    'axmx': 'Android Xamarin SDK',
    'auni': 'Android Unity SDK',
    'aunr': 'Android Unreal SDK',
    'iosx': 'IOS Native SDK',
    'irnx': 'IOS React Native SDK',
    'iflt': 'IOS Flutter SDK',
    'icor': 'IOS Cordova SDK',
    'icap': 'IOS Capacitor SDK',
    'ixmf': 'IOS Xamarin Forms SDK',
    'ixmx': 'IOS Xamarin SDK',
    'iuni': 'IOS Unity SDK',
    'iunr': 'IOS Unreal SDK',
    'jsxx': 'JS SDK',
    'jswp': 'WordPress Platform',
    'jswc':  'Woocommerce Platform',
    'jsmg': 'Magento Platform',
    'jsps': 'PrestaShop Platform',
    'jflt':' JS Flutter SDK',
    'jcap': 'JS Capacitor SDK',
    'jcor': 'JS Cordova SDK',
    'jexp': 'JS React-native SDK'
}

sdk_flavour_map = {
    'e': "Element",
    'd': "Drop",
    'i': "Intent"
}


browser_map = {
    'c': " on Chrome Browser",
    's': " on Safari Browser",
    'm': " on Mozilla Browser",
    'o': " on Opera Browser",
    'w': " on Android Webview",
    'k': " on IOS Webview",
    'b': " on Brave Browser",
    'i': " on Internet Explorer",
    'g': " on Samsung Browser",
    'u': " on UC Browser"
}

os_type_map = {
    'a': " using Android ",
    'i': " using IOS ",
    'w': " using Windows ",
    'm': " using Mac ",
    'l': " using Linux OS "
}
def parse_string(input_string):
    pattern = r'(\w+)-(\w+)-(\w+)-([\w.]+)-([\w.]+)-(\w+)-(\w+)-([\w.]+)-(\w+)-([\w.]+)'
    match = re.match(pattern, input_string)
    print(pattern)
    print(match)
    order_info = ''
    year_verion_used = False
    device_type = ''
    sdk_version = ''
    browser_version = ''
    os_info = ''
    os_version = ''
    browser_info = ''
    if match:
        parsed_data = {
            'api_flavour': match.group(1),
            'sdk': match.group(2),
            'sdk_flavour': match.group(3),
            'sdk_version': match.group(4),
            'framework_version': match.group(5),
            'device_type': match.group(6),
            'browser': match.group(7),
            'browser_version': match.group(8),
            'os_info': match.group(9),
            'os_version': match.group(10)
        }
        print(parsed_data)
        sdk_info = ''
        if(parsed_data['api_flavour']) == 'nga':
            order_info = "This order was created using Next Gen API "

        if(parsed_data['sdk'])  in sdk_map:
            order_info = order_info + ' and processed using '+ sdk_map[parsed_data['sdk']]

        if(parsed_data['sdk_flavour']) in sdk_flavour_map:
            if 'SDK' in order_info:
                order_info = order_info[:-3]
                order_info = order_info + sdk_flavour_map[parsed_data['sdk_flavour']] + " SDK"
            else:
                order_info = order_info + "  "+  sdk_flavour_map[parsed_data['sdk_flavour']]

        sdk_version = "-Version: " + parsed_data['sdk_version']

        if parsed_data['browser'] in browser_map:
            browser_info = browser_map[parsed_data['browser']]
            if 'x' in parsed_data['browser_version']:
                parsed_data['browser_version'] = parsed_data['browser_version'].replace('x','')
            browser_version = "-Version:"+ parsed_data['browser_version']
        if parsed_data['os_info'] in os_type_map and parsed_data['os_version'].isnumeric():
                os_version = " Version: "+ parsed_data['os_version']
        order_info = (order_info + sdk_info + sdk_version + os_type_map[parsed_data['os_info'] ]
                       + device_map[parsed_data['device_type']] + os_version +
                      browser_info + browser_version)
        st.write(order_info)
        return parsed_data
    else:
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.header("Decipher Order Source ")

    # Subheader
    st.subheader("PGapps understand that Order Source is complex, So we have built this for you.")
    order_source = st.text_input("Enter the Order Source here")
    if st.button('Decipher'):
        parse_string(order_source)
