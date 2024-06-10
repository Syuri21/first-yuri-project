import json

data = {
    "info": {
        "name": "JJNET Consortium Dataset",
        "version": "1.0",
        "year": 2022,
        "maker": "JJNET Consortium",
        "date_created": "2022-08-05 05:49:02.276"
    },
    "images": [
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "frameid": 0,
            "width": 1920,
            "height": 1080,
            "filename": "image1.jpg",
            "waterlevel": "1.7m",
            "climate": "맑음",
            "backcolor": "White",
            "deviceType": "CCTV",
            "obstruction": "없음"
        },
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174001",
            "frameid": 1,
            "width": 1920,
            "height": 1080,
            "filename": "image2.jpg",
            "waterlevel": "2.1m",
            "climate": "흐림",
            "backcolor": "Green",
            "deviceType": "스마트폰",
            "obstruction": "나뭇가지"
        }
    ],
    "annotations": [
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "class_id": 0,
            "name": "surface",
            "coordinates": {"x": 100, "y": 150}
        }
    ],
    "categories": [
        {
            "id": 1,
            "mokjaType": "A",
            "width": "30cm",
            "clslevel": "0~5m"
        }
    ]
}

def print_image_info(image):
    print(f"이미지 식별자: {image['uuid']}")
    print(f"프레임 ID: {image['frameid']}")
    print(f"너비: {image['width']}")
    print(f"높이: {image['height']}")
    print(f"파일명: {image['filename']}")
    print(f"수위: {image['waterlevel']}")
    print(f"기상: {image['climate']}")
    print(f"배경 색상: {image['backcolor']}")
    print(f"촬영 장비: {image['deviceType']}")
    print(f"방해 종류: {image['obstruction']}")
    print()

for image in data["images"]:
    print_image_info(image)

def extract_water_levels(data):
    water_levels = []
    for image in data["images"]:
        water_levels.append({
            "uuid": image["uuid"],
            "waterlevel": image["waterlevel"]
        })
    return water_levels

water_levels = extract_water_levels(data)
print("수위 정보:")
for wl in water_levels:
    print(f"UUID: {wl['uuid']}, 수위: {wl['waterlevel']}")