import json

def create_mock_data(data : list[dict], file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    mock_models = [
        {
            "model" : "A",
            "input_cost_per_million" : 0.2,
            "output_cost_per_million" : 0.4,
            "avg_response_time_ms" : 800
        },
        {
            "model" : "B",
            "input_cost_per_million" : 1.0,
            "output_cost_per_million" : 2.0,
            "avg_response_time_ms" : 500
        },
        {
            "model" : "C",
            "input_cost_per_million" : 1.5,
            "output_cost_per_million" : 3.0,
            "avg_response_time_ms" : 150
        },
        {
            "model" : "D",
            "input_cost_per_million" : 5.0,
            "output_cost_per_million" : 15.0,
            "avg_response_time_ms" : 1200
        }
    ]
    file_path = "models.json"
    create_mock_data(mock_models, file_path)