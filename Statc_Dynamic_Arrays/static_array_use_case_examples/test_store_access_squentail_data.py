import store_access_sequential_data

def test_getting_element():
  first_element = store_access_sequential_data.get_element(0)

  assert first_element == 1