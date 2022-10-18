from datetime import datetime

data2 = [
    {"name": "Product A", "id": 29, "dt1": "2022/01/01", "dt2": "01/01/2022"},
    {"name": "Product C", "id": 25, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product B", "id": 21, "dt1": "2022/03/01", "dt2": "01/03/2022"},
    {"name": "Product D", "id": 23, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product F", "id": 22, "dt1": "2022/20/04", "dt2": "20/04/2022"},
    {"name": "Product E", "id": 20, "dt1": "1995/12/29", "dt2": "29/12/1995"},
]


data2.sort(key=lambda value: value["name"])

# print(data2)

data3 = [
    {"name": "Product A", "id": 29, "dt1": "2022/01/01", "dt2": "01/01/2022"},
    {"name": "Product C", "id": 25, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product B", "id": 21, "dt1": "2022/03/01", "dt2": "01/03/2022"},
    {"name": "Product D", "id": 23, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product F", "id": 22, "dt1": "2022/20/04", "dt2": "20/04/2022"},
    {"name": "Product E", "id": 20, "dt1": "1995/12/29", "dt2": "29/12/1995"},
]

data3.sort(key=lambda value: value["name"], reverse=True)

# print(data3)


data4 = [
    {"name": "Product A", "id": 29, "dt1": "2022/01/01", "dt2": "01/01/2022"},
    {"name": "Product C", "id": 25, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product B", "id": 21, "dt1": "2022/03/01", "dt2": "01/03/2022"},
    {"name": "Product D", "id": 23, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product F", "id": 22, "dt1": "2022/20/04", "dt2": "20/04/2022"},
    {"name": "Product E", "id": 20, "dt1": "1995/12/29", "dt2": "29/12/1995"},
]


def order_data(value):
    return value["name"]


data4.sort(key=order_data)

# print(data4)


data5 = [
    {"name": "Product A", "id": 29, "dt1": "2022/01/01", "dt2": "01/01/2022"},
    {"name": "Product C", "id": 25, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product B", "id": 21, "dt1": "2022/03/01", "dt2": "01/03/2022"},
    {"name": "Product D", "id": 23, "dt1": "2022/02/01", "dt2": "01/02/2022"},
    {"name": "Product F", "id": 22, "dt1": "2022/20/04", "dt2": "20/04/2022"},
    {"name": "Product E", "id": 20, "dt1": "1995/12/29", "dt2": "29/12/1995"},
]


def convert_br_date_to_obj(date):
    dt = date.split("/")
    return datetime(
        int(dt[2]),
        int(dt[1]),
        int(
            dt[0],
        ),
    )


def order_data_convert(value):
    return convert_br_date_to_obj(value["dt2"])


data5.sort(key=order_data_convert)

print(data5)
