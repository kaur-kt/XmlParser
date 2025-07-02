
import pandas as pd
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('Menu.xml')
root = tree.getroot()

# Create a list to store dictionaries representing each item
item_list = []
# Iterate through each <MenuItem> element
for menu_elem in root.findall('.//MenuItem'):
    menu_dict = {}
    menu_dict['selection'] = menu_elem.get('selection')
    for child_elem in menu_elem:
        menu_dict[child_elem.tag] = child_elem.text
    item_list.append(menu_dict)
    # Iterate through each <Link> element
    for link_elem in root.findall('.//Link'):
        link_dict = {}
        link_dict['selection'] = link_elem.get('selection')
        count = 0
        for child_elem in link_elem:
            ### NB! Siin kirjutatakse muidu tag Attribute iga kord üle ja kehtima jääb nn viimane väärtus
            if child_elem.tag =='Attribute':
                count = count + 1
                child_elem_plus = child_elem.tag + format(count)
                #print(child_elem.get('name')) 
                #link_dict[child_elem_plus] = child_elem.text
                link_dict[child_elem.get('name')] = child_elem.text
            else:
                link_dict[child_elem.tag] = child_elem.text
            #print(child_elem.tag, child_elem.text)
        #print(link_dict)
        item_list.append(link_dict)



# Create a Pandas DataFrame from the list of dictionaries
df = pd.DataFrame(item_list)

# Display the DataFrame
print(df)
# Save the DataFrame to the output file
df.to_csv('output.txt')

