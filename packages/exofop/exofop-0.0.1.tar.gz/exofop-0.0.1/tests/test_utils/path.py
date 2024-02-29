import os

def get_test_data_dir():
    test_data_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "test_data")
    )

    if not os.path.exists(test_data_dir):
        os.makedirs(test_data_dir, exist_ok=True)

    return test_data_dir
