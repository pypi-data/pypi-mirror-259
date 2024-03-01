from catbox_api import catboxAPI

API_KEY = "YOUR_API_KEY_HERE"

api = catboxAPI(API_KEY)

print("TEST 1: upload_from_url")
file_id_1 = api.upload_from_url("https://i.imgur.com/jIOInlc.png")
print(f"Uploaded file id: {file_id_1}\n")

print("TEST 2: upload_from_path")
file_id_2 = api.upload_from_path("./test_img1.jpg")
print(f"Uploaded file id: {file_id_2}\n")

print("TEST 3: upload_file")
file_id_3 = api.upload_file("test_img2.jpg", open("./test_img2.jpg", "rb"))
print(f"Uploaded file id: {file_id_3}\n")

print(f"TEST 4: delete_file {file_id_3}")
result = api.delete_file(file_id_3)
print(f"{result}\n")

print("TEST 5: create_album")
album_id = api.create_album("catbox_api_test_name", "catbox_api_test_description")
print(f"Created album id: {album_id}\n")

print("TEST 6: upload_file_to_album #1")
file_id_4 = api.upload_file_to_album(album_id, "test_img2.jpg", open("./test_img2.jpg", "rb"))
print(f"Uploaded file id: {file_id_4}\n")

print("TEST 7: upload_file_to_album #2")
file_id_5 = api.upload_file_to_album(album_id, "test_img3.jpg", open("./test_img3.jpg", "rb"))
print(f"Uploaded file id: {file_id_5}\n")

print("TEST 8: get_album_file_ids #1")
result = api.get_album_file_ids(album_id)
print(f"Album file ids: {result}\n")

print(f"TEST 9: delete_file {file_id_4}")
result = api.delete_file(file_id_4)
print(f"{result}\n")

print("TEST 10: get_album_file_ids #2")
result = api.get_album_file_ids(album_id)
print(f"Album file ids: {result}\n")

print(f"TEST 11: delete_album {album_id}")
result = api.delete_album(album_id)
print(f"Deleted album. {result}\n")

print("=== cleanup ===")
print(f"delete_file {file_id_1}")
print(api.delete_file(file_id_1))
print(f"delete_file {file_id_2}")
print(api.delete_file(file_id_2))
print(f"delete_file {file_id_5}")
print(api.delete_file(file_id_5))