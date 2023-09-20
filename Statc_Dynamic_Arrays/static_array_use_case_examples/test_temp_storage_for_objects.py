import temp_storage_for_objects

def test_getting_person():
  billy = temp_storage_for_objects.person_arr[0]
  mandy = temp_storage_for_objects.person_arr[1]
  grim = temp_storage_for_objects.person_arr[2]

  assert billy['name'] == 'billy'
  assert billy['age'] == 10
  assert mandy['name'] == 'mandy'
  assert mandy['age'] == 10
  assert grim['name'] == 'grim'
  assert grim['age'] == 1000
