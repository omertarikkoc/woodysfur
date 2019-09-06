import os
import csv
import json


def read_csv(file_name):
    """
    Reads the csv file and returns the data without header
    """
    data = list(csv.reader(open(file_name)))
    header = data[0]

    print(f"Header: {header}")

    # Rest of the data
    data = data[1:]

    return data


def process_csv_rows(data):
    """
    Process the csv row by row and call the markdown function
    Returns array of markdown templates
    """
    md_templates = []
    for row in data:
        id = row[0]
        title = row[1]
        sale_price = row[3]
        regular_price = row[4]
        categories = row[5]
        image = row[6]

        if sale_price == " " or sale_price == None:
            sale_price = regular_price

        # Process images
        image = json.dumps(image.split(","))
        # images_str = ""
        # for img in images:
        #     img = img.strip()
        #     print(img)
        #     images_str += f'"{img}",'

        # images_str = images_str[-1]
        # print(image)

        # print(id, title, sale_price, regular_price, categories, image)
        md = create_md_template(id, title, sale_price, regular_price, categories, image)
        md_templates.append({"id": id, "template": md})
    return md_templates


def create_md_template(id, title, sale_price, regular_price, categories, image):
    return f'---\ntitle: {title}\ndate: 2017-01-04T15:04:10.000Z\nprice: {regular_price}\nsales_price: {sale_price}\ncategories: ["{categories}"]\nimage: {image}\n---'


def create_files(md_templates):
    counter = 0
    for md in md_templates:
        path = f"product/{str(md['id'])}.md"
        with open(path, "w") as f:
            f.write(md["template"])
            counter += 1
    print(f"Total files created: {counter}")
    return counter


# Main Driver
csv_data = read_csv("product_data.csv")
md_temps = process_csv_rows(csv_data)
create_files(md_temps)

