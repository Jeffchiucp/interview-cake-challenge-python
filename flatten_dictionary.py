def flatten_dictionary(dictionary):

  def items():
  # loop through each item inside the dictionary k, v
      #Appending
      # check if the sub-key and sub-value are
      # inside the flatten_dict(value)
      # join on subkey array
      # add to result
      # clear out prev_keys
    for key, value in dictionary.items():
      if isinstance(value, dict):
        for subkey, subvalue in flatten_dictionary(value).items():
          if key == "":
            yield subkey, subvalue
          yield key + "." + subkey, subvalue
      else:
        yield key, value

  return dict(items())


# test cases 1

dictionary2 = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }


# output: {
#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
#         }

print(flatten_dictionary(dictionary2))