import json

def create_mock_data(data : list[dict], file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    data = [
        {
            "model" : "A",
            "cost" : 0.001,
            "response_time" : 0.4
        },
        {
            "model" : "B",
            "cost" : 0.005,
            "response_time" : 1.2
        },
        {
            "model" : "B",
            "cost" : 0.005,
            "response_time" : 1.2
        }
    ]
    file_path = "models.json"
    create_mock_data(data, file_path)