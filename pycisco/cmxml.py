DIRECTORY_HEADER = '''
<CiscoIPPhoneDirectory>

  <Title>%(title)s</Title>

  <Prompt>%(prompt)s</Prompt>
'''

DIRECTORY_FOOTER = '''
</CiscoIPPhoneDirectory>
'''

DIRECTORY_ENTRY = '''
  <DirectoryEntry>
    <Name>%(name)s</Name>
    <Telephone>%(telephone)s</Telephone>
  </DirectoryEntry>
'''

SOFTKEY_ITEM = '''
<SoftKeyItem>
<Name>%(name)s</Name>
<URL>%(url)s</URL>
<Position>%(position)d</Position>
</SoftKeyItem>
'''

MENU_HEADER = '''
<CiscoIPPhoneMenu>

  <Title>%(title)s</Title>

  <Prompt>%(prompt)s</Prompt>
'''

MENU_ITEM = '''
  <MenuItem>
   <Name>%(name)s</Name>
   <URL>%(url)s</URL>
  </MenuItem>
'''

MENU_FOOTER = '''
</CiscoIPPhoneMenu>
'''

PHONE_STATUS = '''
<CiscoIPPhoneStatus>
<Text>%(text)s</Text>
<LocationX>1</LocationX>
<LocationY>1</LocationY>
<Depth>2</Depth>
<Width>%(width)d</Width>
<Height>%(height)d</Height>
<Data>%(data)s</Data>
</CiscoIPPhoneStatus> 
'''


PHONE_EXECUTE_HEADER = '''
<CiscoIPPhoneExecute>
'''

EXECUTE_ITEM = '''
<ExecuteItem Priority="0" URL="%(url)s"/>
'''

PHONE_EXECUTE_FOOTER = '''
</CiscoIPPhoneExecute>
'''

PHONE_IMAGE = '''
<CiscoIPPhoneImage>
<LocationX>1</LocationX>
<LocationY>1</LocationY>
<Height>%(height)d</Height>
<Width>%(width)d</Width>
<Depth>2</Depth>
<Data>%(data)s</Data>
</CiscoIPPhoneImage>
'''

def create_execute_url(url):
    push_xml = \
        PHONE_EXECUTE_HEADER + \
        EXECUTE_ITEM % {'url': url} + \
        PHONE_EXECUTE_FOOTER
    return push_xml
